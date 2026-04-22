from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from bot.questions import LEVEL_LABELS, LEVEL_EMOJI


def main_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📚 Choose Level", callback_data="menu:levels")],
            [InlineKeyboardButton("📝 Quick Quiz", callback_data="quiz:start")],
            [
                InlineKeyboardButton("📊 My Stats", callback_data="menu:stats"),
                InlineKeyboardButton("ℹ️ About", callback_data="menu:about"),
            ],
        ]
    )


def levels_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(LEVEL_LABELS[1], callback_data="level:1")],
            [InlineKeyboardButton(LEVEL_LABELS[2], callback_data="level:2")],
            [InlineKeyboardButton(LEVEL_LABELS[3], callback_data="level:3")],
            [InlineKeyboardButton("⬅️ Back", callback_data="menu:main")],
        ]
    )


def topics_menu(level: int, topics: list) -> InlineKeyboardMarkup:
    buttons = []
    row = []
    for idx, topic in enumerate(topics):
        row.append(
            InlineKeyboardButton(
                f"{LEVEL_EMOJI[level]} {topic}",
                callback_data=f"topic:{level}:{idx}",
            )
        )
        if len(row) == 2:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
    buttons.append([InlineKeyboardButton("⬅️ Back", callback_data="menu:levels")])
    return InlineKeyboardMarkup(buttons)


def question_actions(question_id: int, has_hint: bool = False) -> InlineKeyboardMarkup:
    buttons = []
    if not has_hint:
        buttons.append(InlineKeyboardButton("💡 Hint", callback_data=f"hint:{question_id}"))
    else:
        buttons.append(InlineKeyboardButton("⬅️ Question", callback_data=f"question_back:{question_id}"))
    buttons.append(InlineKeyboardButton("⬅️ Topics", callback_data="menu:levels"))
    buttons.append(InlineKeyboardButton("🏠 Home", callback_data="menu:main"))
    buttons.append(InlineKeyboardButton("📊 Stats", callback_data="menu:stats"))
    return InlineKeyboardMarkup([buttons[i : i + 2] for i in range(0, len(buttons), 2)])


def answer_result(question_id: int, is_correct: bool) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton("➡️ Next", callback_data=f"next:{question_id}"),
            InlineKeyboardButton("🔄 Retry", callback_data=f"retry:{question_id}"),
        ],
        [
            InlineKeyboardButton("📖 Explanation", callback_data=f"explain:{question_id}"),
            InlineKeyboardButton("⬅️ Topics", callback_data="menu:levels"),
        ],
        [
            InlineKeyboardButton("🏠 Home", callback_data="menu:main"),
        ],
    ]
    return InlineKeyboardMarkup(buttons)


def back_to_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("🏠 Main Menu", callback_data="menu:main")]]
    )


def quiz_options(quiz_id: int, options: list) -> InlineKeyboardMarkup:
    labels = ["A", "B", "C", "D"]
    buttons = []
    for idx, opt in enumerate(options):
        buttons.append(
            InlineKeyboardButton(
                f"{labels[idx]}. {opt}",
                callback_data=f"quiz:answer:{quiz_id}:{idx}",
            )
        )
    return InlineKeyboardMarkup([buttons[i : i + 2] for i in range(0, len(buttons), 2)])


def quiz_next_actions(has_more: bool) -> InlineKeyboardMarkup:
    buttons = []
    if has_more:
        buttons.append(InlineKeyboardButton("➡️ Next Question", callback_data="quiz:next"))
    buttons.append(InlineKeyboardButton("🏠 End Quiz", callback_data="menu:main"))
    return InlineKeyboardMarkup([buttons[i : i + 2] for i in range(0, len(buttons), 2)])


def quiz_start_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🚀 Start Quiz", callback_data="quiz:begin")],
            [InlineKeyboardButton("⬅️ Back", callback_data="menu:main")],
        ]
    )
