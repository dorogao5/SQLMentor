import re
from typing import Optional

from telegram import Update
from telegram.ext import ContextTypes

from bot.i18n_ui import tr, quiz_result_footer
from bot.questions import (
    QUESTIONS,
    get_question_by_id,
    get_topics,
    get_questions_by_topic,
    localize_question,
    get_level_label,
)
from bot.quiz import QUIZ_QUESTIONS, localize_quiz_question
from bot.database import (
    get_or_create_user,
    get_user_locale,
    set_user_locale,
    record_attempt,
    get_user_stats,
    get_progress_for_user,
)
from bot.keyboards import (
    main_menu,
    levels_menu,
    topics_menu,
    question_actions,
    answer_result,
    back_to_menu,
    quiz_options,
    quiz_next_actions,
    quiz_start_menu,
    language_menu,
    settings_menu,
)
from bot.config import logger


def normalize_sql(sql: str) -> str:
    sql = sql.lower().strip()
    sql = sql.rstrip(";")
    sql = re.sub(r"\s+", " ", sql)
    return sql


def escape_html(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


async def user_locale(user_id: int) -> Optional[str]:
    loc = await get_user_locale(user_id)
    return loc if loc in ("en", "ru") else None


def build_question_text(q: dict, lang: str) -> str:
    level_label = get_level_label(q["level"], lang)
    return (
        f"<b>{level_label} — {escape_html(q['topic'])}</b>\n\n"
        f"📌 <b>{escape_html(q['title'])}</b>\n\n"
        f"{tr(lang, 'task_label')}\n{escape_html(q['question'])}\n\n"
        f"{tr(lang, 'schema_label')}\n<pre>{escape_html(q['schema'])}</pre>\n\n"
        f"{tr(lang, 'send_sql')}"
    )


def build_stats_text(stats: dict, lang: str) -> str:
    return (
        f"{tr(lang, 'stats_title')}\n"
        + tr(
            lang,
            "stats_line_attempts",
            total_attempts=stats["total_attempts"],
        )
        + tr(
            lang,
            "stats_line_correct",
            total_correct=stats["total_correct"],
        )
        + tr(
            lang,
            "stats_line_solved",
            solved=stats["solved"],
            total_questions=stats["total_questions"],
        )
        + tr(
            lang,
            "stats_line_completion",
            completion_pct=stats["completion_pct"],
        )
        + tr(
            lang,
            "stats_line_streak",
            streak=stats["streak"],
        )
        + tr(lang, "stats_footer")
    )


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await get_or_create_user(user.id, user.username, user.first_name)
    loc = await user_locale(user.id)
    if not loc:
        await update.message.reply_text(
            tr("en", "pick_language"),
            reply_markup=language_menu(),
            parse_mode="HTML",
        )
        return
    text = tr(
        loc,
        "welcome",
        name=escape_html(user.first_name or ("learner" if loc == "en" else "ученик")),
    )
    await update.message.reply_text(
        text, reply_markup=main_menu(loc), parse_mode="HTML"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    loc = await user_locale(user_id)
    lang = loc or "en"
    await update.message.reply_text(
        tr(lang, "help_full"),
        reply_markup=back_to_menu(lang),
        parse_mode="HTML",
    )


async def send_question(query, context: ContextTypes.DEFAULT_TYPE, q: dict, lang: str):
    context.user_data["current_question_id"] = q["id"]
    qd = localize_question(q, lang)
    text = build_question_text(qd, lang)
    await query.edit_message_text(
        text, reply_markup=question_actions(q["id"], lang), parse_mode="HTML"
    )


async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    user_id = update.effective_user.id

    if data.startswith("setlang:"):
        chosen = data.split(":")[1]
        if chosen not in ("en", "ru"):
            await query.answer()
            return
        await set_user_locale(user_id, chosen)
        await query.answer(tr(chosen, "toast_language_set"))
        user = update.effective_user
        text = tr(
            chosen,
            "welcome",
            name=escape_html(user.first_name or ("learner" if chosen == "en" else "ученик")),
        )
        await query.edit_message_text(
            text, reply_markup=main_menu(chosen), parse_mode="HTML"
        )
        return

    await query.answer()
    lang = await user_locale(user_id)
    if lang is None:
        await query.edit_message_text(
            tr("en", "need_language"),
            reply_markup=language_menu(),
            parse_mode="HTML",
        )
        return

    if data == "menu:main":
        await query.edit_message_text(
            tr(lang, "main_menu_title"),
            reply_markup=main_menu(lang),
            parse_mode="HTML",
        )

    elif data == "menu:settings":
        await query.edit_message_text(
            tr(lang, "settings_title"),
            reply_markup=settings_menu(lang),
            parse_mode="HTML",
        )

    elif data == "menu:levels":
        await query.edit_message_text(
            tr(lang, "levels_title"),
            reply_markup=levels_menu(lang),
            parse_mode="HTML",
        )

    elif data == "menu:stats":
        stats = await get_user_stats(user_id, total_questions=len(QUESTIONS))
        text = build_stats_text(stats, lang)
        await query.edit_message_text(
            text, reply_markup=back_to_menu(lang), parse_mode="HTML"
        )

    elif data == "menu:about":
        text = tr(lang, "about_title") + tr(lang, "about_body")
        await query.edit_message_text(
            text, reply_markup=back_to_menu(lang), parse_mode="HTML"
        )

    elif data.startswith("level:"):
        level = int(data.split(":")[1])
        topics = get_topics(level)
        text = tr(
            lang,
            "topics_title",
            level=get_level_label(level, lang),
        )
        await query.edit_message_text(
            text, reply_markup=topics_menu(level, topics, lang), parse_mode="HTML"
        )

    elif data.startswith("topic:"):
        parts = data.split(":")
        level = int(parts[1])
        topic_idx = int(parts[2])
        topics = get_topics(level)
        topic = topics[topic_idx]
        questions = get_questions_by_topic(level, topic)
        solved = await get_progress_for_user(user_id)
        q = None
        for question in questions:
            if question["id"] not in solved:
                q = question
                break
        if q is None:
            q = questions[0]
        await send_question(query, context, q, lang)

    elif data.startswith("hint:"):
        qid = int(data.split(":")[1])
        q = get_question_by_id(qid)
        if q:
            q = localize_question(q, lang)
            await query.edit_message_text(
                tr(lang, "hint_intro")
                + escape_html(q["hint"])
                + tr(lang, "hint_footer"),
                reply_markup=question_actions(qid, lang, has_hint=True),
                parse_mode="HTML",
            )

    elif data.startswith("question_back:"):
        qid = int(data.split(":")[1])
        q = get_question_by_id(qid)
        if q:
            await send_question(query, context, q, lang)

    elif data.startswith("next:"):
        current_qid = int(data.split(":")[1])
        current = get_question_by_id(current_qid)
        level = current["level"]
        topic = current["topic"]
        questions = get_questions_by_topic(level, topic)
        idx = next((i for i, q in enumerate(questions) if q["id"] == current_qid), -1)
        next_q = questions[idx + 1] if idx >= 0 and idx + 1 < len(questions) else None
        if next_q:
            await send_question(query, context, next_q, lang)
        else:
            await query.edit_message_text(
                tr(lang, "topic_complete"),
                reply_markup=levels_menu(lang),
                parse_mode="HTML",
            )

    elif data.startswith("retry:"):
        qid = int(data.split(":")[1])
        q = get_question_by_id(qid)
        await send_question(query, context, q, lang)

    elif data.startswith("explain:"):
        qid = int(data.split(":")[1])
        q = get_question_by_id(qid)
        q = localize_question(q, lang)
        text = (
            tr(lang, "explain_title")
            + escape_html(q["explanation"])
            + "\n\n"
            + tr(lang, "correct_answer_label")
            + f"<pre>{escape_html(q['correct_answer'])}</pre>"
        )
        await query.edit_message_text(
            text,
            reply_markup=answer_result(qid, lang, is_correct=True),
            parse_mode="HTML",
        )

    elif data == "quiz:start":
        await query.edit_message_text(
            tr(lang, "quiz_intro"),
            reply_markup=quiz_start_menu(lang),
            parse_mode="HTML",
        )

    elif data == "quiz:begin":
        await start_quiz_session(query, context, lang)

    elif data.startswith("quiz:answer:"):
        parts = data.split(":")
        quiz_id = int(parts[2])
        answer_idx = int(parts[3])
        await check_quiz_answer(query, context, quiz_id, answer_idx, lang)

    elif data == "quiz:next":
        st = context.user_data.get("quiz")
        quiz_lang = st.get("lang", lang) if st else lang
        await show_quiz_question(query, context, quiz_lang)


async def start_quiz_session(query, context: ContextTypes.DEFAULT_TYPE, lang: str):
    import random

    selected = random.sample(QUIZ_QUESTIONS, min(10, len(QUIZ_QUESTIONS)))
    context.user_data["quiz"] = {
        "questions": selected,
        "index": 0,
        "score": 0,
        "lang": lang,
    }
    await show_quiz_question(query, context, lang)


def build_quiz_question_message(q: dict, lang: str, n: int, total: int) -> str:
    letters = ("A", "B", "C", "D")
    parts = [
        tr(lang, "quiz_question_header", n=n, total=total),
        escape_html(q["question"]),
        "",
    ]
    for i, opt in enumerate(q["options"]):
        letter = letters[i] if i < len(letters) else str(i + 1)
        parts.append(f"<b>{letter}</b>. {escape_html(opt)}")
    parts.extend(["", tr(lang, "quiz_pick_letter")])
    return "\n".join(parts)


async def show_quiz_question(query, context: ContextTypes.DEFAULT_TYPE, lang: str):
    quiz_state = context.user_data.get("quiz")
    if not quiz_state:
        await query.edit_message_text(
            tr(lang, "quiz_expired"),
            reply_markup=quiz_start_menu(lang),
            parse_mode="HTML",
        )
        return

    idx = quiz_state["index"]
    if idx >= len(quiz_state["questions"]):
        score = quiz_state["score"]
        total = len(quiz_state["questions"])
        acc = round((score / total) * 100, 1) if total else 0
        footer = quiz_result_footer(lang, score, total)
        text = tr(
            lang,
            "quiz_complete",
            score=score,
            total=total,
            acc=acc,
            footer=footer,
        )
        await query.edit_message_text(
            text, reply_markup=back_to_menu(lang), parse_mode="HTML"
        )
        context.user_data.pop("quiz", None)
        return

    q = quiz_state["questions"][idx]
    q = localize_quiz_question(q, lang)
    text = build_quiz_question_message(
        q, lang, idx + 1, len(quiz_state["questions"])
    )
    await query.edit_message_text(
        text,
        reply_markup=quiz_options(q["id"], len(q["options"])),
        parse_mode="HTML",
    )


async def check_quiz_answer(
    query, context: ContextTypes.DEFAULT_TYPE, quiz_id: int, answer_idx: int, lang: str
):
    quiz_state = context.user_data.get("quiz")
    if not quiz_state:
        await query.answer(tr(lang, "quiz_expired_alert"), show_alert=True)
        return

    idx = quiz_state["index"]
    q = quiz_state["questions"][idx]
    if q["id"] != quiz_id:
        await query.answer(tr(lang, "quiz_mismatch_alert"), show_alert=True)
        context.user_data.pop("quiz", None)
        return

    q_display = localize_quiz_question(q, lang)
    is_correct = answer_idx == q["correct_index"]
    if is_correct:
        quiz_state["score"] += 1
        result_text = tr(lang, "quiz_correct")
    else:
        correct_label = ["A", "B", "C", "D"][q["correct_index"]]
        result_text = tr(lang, "quiz_wrong", label=correct_label)

    quiz_state["index"] += 1
    has_more = quiz_state["index"] < len(quiz_state["questions"])

    text = (
        f"{result_text}\n\n"
        + tr(lang, "quiz_explain")
        + escape_html(q_display["explanation"])
    )
    await query.edit_message_text(
        text,
        reply_markup=quiz_next_actions(has_more, lang),
        parse_mode="HTML",
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = await user_locale(user_id)
    if lang is None:
        await update.message.reply_text(
            tr("en", "need_language"),
            reply_markup=language_menu(),
            parse_mode="HTML",
        )
        return

    current_qid = context.user_data.get("current_question_id")
    if not current_qid:
        await update.message.reply_text(
            tr(lang, "no_question"),
            reply_markup=back_to_menu(lang),
            parse_mode="HTML",
        )
        return

    q = get_question_by_id(current_qid)
    user_answer = update.message.text or ""
    normalized_user = normalize_sql(user_answer)
    normalized_correct = normalize_sql(q["correct_answer"])

    is_correct = normalized_user == normalized_correct

    await record_attempt(user_id, current_qid, user_answer, is_correct)

    name = escape_html(
        update.effective_user.first_name or ("learner" if lang == "en" else "ученик")
    )
    if is_correct:
        text = tr(
            lang,
            "correct_reply",
            name=name,
            answer=escape_html(user_answer),
        )
    else:
        text = tr(
            lang,
            "wrong_reply",
            answer=escape_html(user_answer),
        )

    await update.message.reply_text(
        text,
        reply_markup=answer_result(current_qid, lang, is_correct),
        parse_mode="HTML",
    )


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error("Exception while handling an update:", exc_info=context.error)
