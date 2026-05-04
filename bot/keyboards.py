from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot.i18n_ui import tr
from bot.questions import LEVEL_EMOJI, get_level_label, get_topic_display


def language_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🇬🇧 English", callback_data="setlang:en"),
                InlineKeyboardButton("🇷🇺 Русский", callback_data="setlang:ru"),
            ]
        ]
    )


def main_menu(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(tr(lang, "btn_choose_level"), callback_data="menu:levels")],
            [InlineKeyboardButton(tr(lang, "btn_quiz"), callback_data="quiz:start")],
            [
                InlineKeyboardButton(tr(lang, "btn_stats"), callback_data="menu:stats"),
                InlineKeyboardButton(tr(lang, "btn_about"), callback_data="menu:about"),
            ],
            [InlineKeyboardButton(tr(lang, "btn_settings"), callback_data="menu:settings")],
        ]
    )


def settings_menu(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🇬🇧 English", callback_data="setlang:en"),
                InlineKeyboardButton("🇷🇺 Русский", callback_data="setlang:ru"),
            ],
            [InlineKeyboardButton(tr(lang, "btn_back"), callback_data="menu:main")],
        ]
    )


def levels_menu(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(get_level_label(1, lang), callback_data="level:1")],
            [InlineKeyboardButton(get_level_label(2, lang), callback_data="level:2")],
            [InlineKeyboardButton(get_level_label(3, lang), callback_data="level:3")],
            [InlineKeyboardButton(tr(lang, "btn_back"), callback_data="menu:main")],
        ]
    )


def topics_menu(level: int, topics: list, lang: str) -> InlineKeyboardMarkup:
    buttons = []
    row = []
    for idx, topic in enumerate(topics):
        label = get_topic_display(level, topic, lang)
        row.append(
            InlineKeyboardButton(
                f"{LEVEL_EMOJI[level]} {label}",
                callback_data=f"topic:{level}:{idx}",
            )
        )
        if len(row) == 2:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
    buttons.append([InlineKeyboardButton(tr(lang, "btn_back"), callback_data="menu:levels")])
    return InlineKeyboardMarkup(buttons)


def question_actions(question_id: int, lang: str, has_hint: bool = False) -> InlineKeyboardMarkup:
    buttons = []
    if not has_hint:
        buttons.append(
            InlineKeyboardButton(tr(lang, "btn_hint"), callback_data=f"hint:{question_id}")
        )
    else:
        buttons.append(
            InlineKeyboardButton(
                tr(lang, "btn_question"), callback_data=f"question_back:{question_id}"
            )
        )
    buttons.append(InlineKeyboardButton(tr(lang, "btn_topics"), callback_data="menu:levels"))
    buttons.append(InlineKeyboardButton(tr(lang, "btn_home"), callback_data="menu:main"))
    buttons.append(InlineKeyboardButton(tr(lang, "btn_stats"), callback_data="menu:stats"))
    return InlineKeyboardMarkup([buttons[i : i + 2] for i in range(0, len(buttons), 2)])


def answer_result(question_id: int, lang: str, is_correct: bool) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(tr(lang, "btn_next"), callback_data=f"next:{question_id}"),
            InlineKeyboardButton(tr(lang, "btn_retry"), callback_data=f"retry:{question_id}"),
        ],
        [
            InlineKeyboardButton(tr(lang, "btn_explain"), callback_data=f"explain:{question_id}"),
            InlineKeyboardButton(tr(lang, "btn_topics"), callback_data="menu:levels"),
        ],
        [
            InlineKeyboardButton(tr(lang, "btn_home"), callback_data="menu:main"),
        ],
    ]
    return InlineKeyboardMarkup(buttons)


def back_to_menu(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(tr(lang, "btn_main_menu"), callback_data="menu:main")]]
    )


def quiz_options(quiz_id: int, num_choices: int) -> InlineKeyboardMarkup:
    labels = ("A", "B", "C", "D")
    row = [
        InlineKeyboardButton(
            labels[i],
            callback_data=f"quiz:answer:{quiz_id}:{i}",
        )
        for i in range(min(num_choices, len(labels)))
    ]
    return InlineKeyboardMarkup([row])


def quiz_next_actions(has_more: bool, lang: str) -> InlineKeyboardMarkup:
    buttons = []
    if has_more:
        buttons.append(
            InlineKeyboardButton(tr(lang, "btn_quiz_next"), callback_data="quiz:next")
        )
    buttons.append(InlineKeyboardButton(tr(lang, "btn_quiz_end"), callback_data="menu:main"))
    return InlineKeyboardMarkup([buttons[i : i + 2] for i in range(0, len(buttons), 2)])


def quiz_start_menu(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(tr(lang, "btn_quiz_start"), callback_data="quiz:begin")],
            [InlineKeyboardButton(tr(lang, "btn_back"), callback_data="menu:main")],
        ]
    )
