import re
from telegram import Update
from telegram.ext import ContextTypes

from bot.questions import (
    LEVEL_LABELS,
    QUESTIONS,
    get_question_by_id,
    get_topics,
    get_questions_by_topic,
)
from bot.quiz import QUIZ_QUESTIONS, get_quiz_by_id
from bot.database import (
    get_or_create_user,
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


def build_question_text(q: dict) -> str:
    return (
        f"<b>{LEVEL_LABELS[q['level']]} — {escape_html(q['topic'])}</b>\n\n"
        f"📌 <b>{escape_html(q['title'])}</b>\n\n"
        f"📝 <b>Task:</b>\n{escape_html(q['question'])}\n\n"
        f"🗂️ <b>Schema:</b>\n<pre>{escape_html(q['schema'])}</pre>\n\n"
        f"✍️ Send your SQL query as a reply."
    )


def build_stats_text(stats: dict) -> str:
    return (
        f"📊 <b>Your Statistics</b>\n\n"
        f"• Total exercises attempted: {stats['total_attempts']}\n"
        f"• Correct answers: {stats['total_correct']}\n"
        f"• Exercises solved: {stats['solved']} / {stats['total_questions']}\n"
        f"• Completion: {stats['completion_pct']}%\n"
        f"• Current streak: {stats['streak']} 🔥\n\n"
        f"Keep practicing to improve your SQL skills!"
    )


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await get_or_create_user(user.id, user.username, user.first_name)
    text = (
        f"👋 Hello, {escape_html(user.first_name or 'learner')}! Welcome to <b>SQLMentor</b> — "
        f"your personal SQL trainer.\n\n"
        f"Here you can practice SQL across three difficulty levels:\n"
        f"🟢 Beginner\n🟡 Intermediate\n🔴 Advanced\n\n"
        f"Choose an option below to get started!"
    )
    await update.message.reply_text(text, reply_markup=main_menu(), parse_mode="HTML")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "ℹ️ <b>SQLMentor Help</b>\n\n"
        "<b>Available commands:</b>\n"
        "/start — Start the bot and open the main menu\n"
        "/help — Show this help message\n\n"
        "<b>How to use:</b>\n"
        "1. Tap <b>📚 Choose Level</b> to pick a difficulty.\n"
        "2. Select a topic you want to practice.\n"
        "3. Read the schema and task, then send your SQL query.\n"
        "4. Get instant feedback, view explanations, and move to the next exercise.\n"
        "5. Tap <b>📊 My Stats</b> anytime to see your progress.\n\n"
        "Tips:\n"
        "• Write queries in a single message.\n"
        "• Column and table names must match the schema exactly.\n"
        "• You can use 💡 <b>Hint</b> if you get stuck."
    )
    await update.message.reply_text(text, reply_markup=back_to_menu(), parse_mode="HTML")


async def send_question(query, context: ContextTypes.DEFAULT_TYPE, q: dict):
    context.user_data["current_question_id"] = q["id"]
    text = build_question_text(q)
    await query.edit_message_text(text, reply_markup=question_actions(q["id"]), parse_mode="HTML")


async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    user_id = update.effective_user.id

    if data == "menu:main":
        text = (
            "🏠 <b>Main Menu</b>\n\n"
            "Choose an option below to continue your SQL journey!"
        )
        await query.edit_message_text(text, reply_markup=main_menu(), parse_mode="HTML")

    elif data == "menu:levels":
        await query.edit_message_text(
            "📚 <b>Choose a Level</b>\n\nPick the difficulty that suits you best:",
            reply_markup=levels_menu(),
            parse_mode="HTML",
        )

    elif data == "menu:stats":
        stats = await get_user_stats(user_id, total_questions=len(QUESTIONS))
        text = build_stats_text(stats)
        await query.edit_message_text(text, reply_markup=back_to_menu(), parse_mode="HTML")

    elif data == "menu:about":
        text = (
            "ℹ️ <b>About SQLMentor</b>\n\n"
            "SQLMentor is a lightweight Telegram bot designed to help you learn and practice SQL interactively.\n"
            "• 45 hand-picked exercises\n"
            "• 3 difficulty levels\n"
            "• Instant feedback and explanations\n"
            "• Progress tracking\n\n"
            "Built with ❤️ using Python & SQLite."
        )
        await query.edit_message_text(text, reply_markup=back_to_menu(), parse_mode="HTML")

    elif data.startswith("level:"):
        level = int(data.split(":")[1])
        topics = get_topics(level)
        text = (
            f"{LEVEL_LABELS[level]} — <b>Select a Topic</b>\n\n"
            f"Choose a topic to practice:"
        )
        await query.edit_message_text(text, reply_markup=topics_menu(level, topics), parse_mode="HTML")

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
        await send_question(query, context, q)

    elif data.startswith("hint:"):
        qid = int(data.split(":")[1])
        q = get_question_by_id(qid)
        if q:
            await query.edit_message_text(
                f"💡 <b>Hint</b>\n\n{escape_html(q['hint'])}\n\nSend your SQL answer as a text message.",
                reply_markup=question_actions(qid, has_hint=True),
                parse_mode="HTML",
            )

    elif data.startswith("question_back:"):
        qid = int(data.split(":")[1])
        q = get_question_by_id(qid)
        if q:
            await send_question(query, context, q)

    elif data.startswith("next:"):
        current_qid = int(data.split(":")[1])
        current = get_question_by_id(current_qid)
        level = current["level"]
        topic = current["topic"]
        questions = get_questions_by_topic(level, topic)
        idx = next((i for i, q in enumerate(questions) if q["id"] == current_qid), -1)
        next_q = questions[idx + 1] if idx >= 0 and idx + 1 < len(questions) else None
        if next_q:
            await send_question(query, context, next_q)
        else:
            text = (
                "🎉 <b>Topic Complete!</b>\n\n"
                "You've reached the end of this topic. Great job!\n\n"
                "Select another topic or level to keep practicing."
            )
            await query.edit_message_text(text, reply_markup=levels_menu(), parse_mode="HTML")

    elif data.startswith("retry:"):
        qid = int(data.split(":")[1])
        q = get_question_by_id(qid)
        await send_question(query, context, q)

    elif data.startswith("explain:"):
        qid = int(data.split(":")[1])
        q = get_question_by_id(qid)
        text = (
            f"📖 <b>Explanation</b>\n\n"
            f"{escape_html(q['explanation'])}\n\n"
            f"<b>Correct answer:</b>\n<pre>{escape_html(q['correct_answer'])}</pre>"
        )
        await query.edit_message_text(text, reply_markup=answer_result(qid, is_correct=True), parse_mode="HTML")

    elif data == "quiz:start":
        text = (
            "📝 <b>Quick Quiz</b>\n\n"
            "Test your SQL knowledge with multiple-choice questions!\n"
            "• Instant feedback\n"
            "• Explanations for every answer\n\n"
            "Ready to begin?"
        )
        await query.edit_message_text(text, reply_markup=quiz_start_menu(), parse_mode="HTML")

    elif data == "quiz:begin":
        await start_quiz_session(query, context)

    elif data.startswith("quiz:answer:"):
        parts = data.split(":")
        quiz_id = int(parts[2])
        answer_idx = int(parts[3])
        await check_quiz_answer(query, context, quiz_id, answer_idx)

    elif data == "quiz:next":
        await show_quiz_question(query, context)


async def start_quiz_session(query, context: ContextTypes.DEFAULT_TYPE):
    import random
    selected = random.sample(QUIZ_QUESTIONS, min(10, len(QUIZ_QUESTIONS)))
    context.user_data["quiz"] = {
        "questions": selected,
        "index": 0,
        "score": 0,
    }
    await show_quiz_question(query, context)


async def show_quiz_question(query, context: ContextTypes.DEFAULT_TYPE):
    quiz_state = context.user_data.get("quiz")
    if not quiz_state:
        await query.edit_message_text(
            "Quiz session expired. Start a new one!",
            reply_markup=quiz_start_menu(),
            parse_mode="HTML",
        )
        return

    idx = quiz_state["index"]
    if idx >= len(quiz_state["questions"]):
        score = quiz_state["score"]
        total = len(quiz_state["questions"])
        text = (
            f"🎉 <b>Quiz Complete!</b>\n\n"
            f"Your score: <b>{score} / {total}</b>\n"
            f"Accuracy: <b>{round((score/total)*100, 1) if total else 0}%</b>\n\n"
            f"{'🔥 Excellent work!' if score == total else '💪 Keep practicing!' if score >= total/2 else '📚 Review the basics and try again!'}"
        )
        await query.edit_message_text(text, reply_markup=back_to_menu(), parse_mode="HTML")
        context.user_data.pop("quiz", None)
        return

    q = quiz_state["questions"][idx]
    text = (
        f"📝 <b>Question {idx + 1} of {len(quiz_state['questions'])}</b>\n\n"
        f"{escape_html(q['question'])}"
    )
    await query.edit_message_text(
        text,
        reply_markup=quiz_options(q["id"], q["options"]),
        parse_mode="HTML",
    )


async def check_quiz_answer(query, context: ContextTypes.DEFAULT_TYPE, quiz_id: int, answer_idx: int):
    quiz_state = context.user_data.get("quiz")
    if not quiz_state:
        await query.answer("Quiz session expired.", show_alert=True)
        return

    idx = quiz_state["index"]
    q = quiz_state["questions"][idx]
    if q["id"] != quiz_id:
        await query.answer("Question mismatch. Restarting quiz.", show_alert=True)
        context.user_data.pop("quiz", None)
        return

    is_correct = answer_idx == q["correct_index"]
    if is_correct:
        quiz_state["score"] += 1
        result_text = "✅ <b>Correct!</b>"
    else:
        correct_label = ["A", "B", "C", "D"][q["correct_index"]]
        result_text = f"❌ <b>Wrong!</b> The correct answer was <b>{correct_label}</b>."

    quiz_state["index"] += 1
    has_more = quiz_state["index"] < len(quiz_state["questions"])

    text = (
        f"{result_text}\n\n"
        f"📖 <b>Explanation:</b>\n{escape_html(q['explanation'])}"
    )
    await query.edit_message_text(
        text,
        reply_markup=quiz_next_actions(has_more),
        parse_mode="HTML",
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    current_qid = context.user_data.get("current_question_id")
    if not current_qid:
        await update.message.reply_text(
            "Please select a question from the menu first.",
            reply_markup=back_to_menu(),
        )
        return

    q = get_question_by_id(current_qid)
    user_answer = update.message.text or ""
    normalized_user = normalize_sql(user_answer)
    normalized_correct = normalize_sql(q["correct_answer"])

    is_correct = normalized_user == normalized_correct

    await record_attempt(user_id, current_qid, user_answer, is_correct)

    if is_correct:
        text = (
            f"✅ <b>Correct!</b>\n\n"
            f"Great job, {escape_html(update.effective_user.first_name or 'learner')}!\n\n"
            f"<b>Your answer:</b>\n<pre>{escape_html(user_answer)}</pre>"
        )
    else:
        text = (
            f"❌ <b>Not quite.</b>\n\n"
            f"Don't worry, keep trying!\n\n"
            f"<b>Your answer:</b>\n<pre>{escape_html(user_answer)}</pre>\n\n"
            f"Tip: Check your syntax and column names against the schema above."
        )

    await update.message.reply_text(
        text,
        reply_markup=answer_result(current_qid, is_correct),
        parse_mode="HTML",
    )


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error("Exception while handling an update:", exc_info=context.error)
