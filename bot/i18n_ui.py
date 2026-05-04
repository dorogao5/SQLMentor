# -*- coding: utf-8 -*-
"""UI strings for SQLMentor (English / Russian)."""

STRINGS = {
    "en": {
        "pick_language": "🌐 <b>Choose language</b>\n\nPick English or Russian — you can change this later in Settings.",
        "toast_language_set": "Saved!",
        "welcome": (
            "👋 Hello, {name}! Welcome to <b>SQLMentor</b> — "
            "your personal SQL trainer.\n\n"
            "Here you can practice SQL across three difficulty levels:\n"
            "🟢 Beginner\n🟡 Intermediate\n🔴 Advanced\n\n"
            "Choose an option below to get started!"
        ),
        "main_menu_title": "🏠 <b>Main Menu</b>\n\nChoose an option below to continue your SQL journey!",
        "levels_title": "📚 <b>Choose a Level</b>\n\nPick the difficulty that suits you best:",
        "topics_title": "{level} — <b>Select a Topic</b>\n\nChoose a topic to practice:",
        "stats_title": "📊 <b>Your Statistics</b>\n",
        "stats_line_attempts": "• Total exercises attempted: {total_attempts}\n",
        "stats_line_correct": "• Correct answers: {total_correct}\n",
        "stats_line_solved": "• Exercises solved: {solved} / {total_questions}\n",
        "stats_line_completion": "• Completion: {completion_pct}%\n",
        "stats_line_streak": "• Current streak: {streak} 🔥\n\n",
        "stats_footer": "Keep practicing to improve your SQL skills!",
        "about_title": "ℹ️ <b>About SQLMentor</b>\n\n",
        "about_body": (
            "SQLMentor is a lightweight Telegram bot for interactive SQL practice.\n"
            "• 90 hand-picked exercises\n"
            "• 3 difficulty levels\n"
            "• Instant feedback and explanations\n"
            "• Progress tracking\n\n"
            "Built with ❤️ using Python & SQLite.\n\n"
            "Made by <b>APM+ team</b>."
        ),
        "help_full": (
            "ℹ️ <b>SQLMentor Help</b>\n\n"
            "<b>Commands:</b>\n"
            "/start — Main menu\n"
            "/help — This message\n\n"
            "<b>How to use:</b>\n"
            "1. Tap <b>📚 Choose Level</b>.\n"
            "2. Pick a topic.\n"
            "3. Read the schema and task, then send your SQL.\n"
            "4. Get feedback, explanations, and move on.\n"
            "5. Tap <b>📊 My Stats</b> for progress.\n\n"
            "Tips:\n"
            "• One query per message.\n"
            "• Names must match the schema.\n"
            "• Use 💡 <b>Hint</b> if stuck."
        ),
        "topic_complete": (
            "🎉 <b>Topic Complete!</b>\n\n"
            "You've reached the end of this topic. Great job!\n\n"
            "Pick another topic or level to keep practicing."
        ),
        "hint_intro": "💡 <b>Hint</b>\n\n",
        "hint_footer": "\n\nSend your SQL answer as a text message.",
        "explain_title": "📖 <b>Explanation</b>\n\n",
        "correct_answer_label": "<b>Correct answer:</b>\n",
        "quiz_intro": (
            "📝 <b>Quick Quiz</b>\n\n"
            "Multiple-choice SQL questions.\n"
            "• Instant feedback\n"
            "• Explanation for each answer\n\n"
            "Ready?"
        ),
        "quiz_expired": "Quiz session expired. Start a new one!",
        "quiz_complete": (
            "🎉 <b>Quiz Complete!</b>\n\n"
            "Your score: <b>{score} / {total}</b>\n"
            "Accuracy: <b>{acc}%</b>\n\n"
            "{footer}"
        ),
        "quiz_footer_perfect": "🔥 Excellent work!",
        "quiz_footer_good": "💪 Keep practicing!",
        "quiz_footer_low": "📚 Review the basics and try again!",
        "quiz_question_header": "📝 <b>Question {n} of {total}</b>\n\n",
        "quiz_pick_letter": "👆 Tap <b>A</b>, <b>B</b>, <b>C</b>, or <b>D</b> below.",
        "quiz_wrong": "❌ <b>Wrong!</b> The correct answer was <b>{label}</b>.",
        "quiz_explain": "📖 <b>Explanation:</b>\n",
        "quiz_mismatch_alert": "Question mismatch. Restarting quiz.",
        "quiz_expired_alert": "Quiz session expired.",
        "correct_reply": (
            "✅ <b>Correct!</b>\n\n"
            "Great job, {name}!\n\n"
            "<b>Your answer:</b>\n<pre>{answer}</pre>"
        ),
        "wrong_reply": (
            "❌ <b>Not quite.</b>\n\n"
            "Don't worry, keep trying!\n\n"
            "<b>Your answer:</b>\n<pre>{answer}</pre>\n\n"
            "Tip: Check syntax and column names against the schema."
        ),
        "no_question": "Please select a question from the menu first.",
        "need_language": "Please tap /start and choose a language.",
        "settings_title": "⚙️ <b>Settings</b>\n\nLanguage / Язык:",
        "task_label": "📝 <b>Task:</b>",
        "schema_label": "🗂️ <b>Schema:</b>",
        "send_sql": "✍️ Send your SQL query as a reply.",
        "btn_choose_level": "📚 Choose Level",
        "btn_quiz": "📝 Quick Quiz",
        "btn_stats": "📊 My Stats",
        "btn_about": "ℹ️ About",
        "btn_settings": "⚙️ Settings",
        "btn_back": "⬅️ Back",
        "btn_home": "🏠 Home",
        "btn_main_menu": "🏠 Main Menu",
        "btn_hint": "💡 Hint",
        "btn_question": "⬅️ Question",
        "btn_topics": "⬅️ Topics",
        "btn_next": "➡️ Next",
        "btn_retry": "🔄 Retry",
        "btn_explain": "📖 Explanation",
        "btn_quiz_start": "🚀 Start Quiz",
        "btn_quiz_next": "➡️ Next Question",
        "btn_quiz_end": "🏠 End Quiz",
        "level_beginner": "🟢 Beginner",
        "level_intermediate": "🟡 Intermediate",
        "level_advanced": "🔴 Advanced",
    },
    "ru": {
        "pick_language": "🌐 <b>Выберите язык</b>\n\nEnglish или Русский — сменить можно позже в настройках.",
        "toast_language_set": "Сохранено!",
        "welcome": (
            "👋 Здравствуйте, {name}! Добро пожаловать в <b>SQLMentor</b> — "
            "вашего интерактивного тренера по SQL.\n\n"
            "Три уровня сложности:\n"
            "🟢 Начинающий\n🟡 Средний\n🔴 Продвинутый\n\n"
            "Выберите действие ниже."
        ),
        "main_menu_title": "🏠 <b>Главное меню</b>\n\nВыберите пункт, чтобы продолжить.",
        "levels_title": "📚 <b>Уровень</b>\n\nВыберите сложность:",
        "topics_title": "{level} — <b>Тема</b>\n\nВыберите тему для практики:",
        "stats_title": "📊 <b>Ваша статистика</b>\n",
        "stats_line_attempts": "• Всего попыток: {total_attempts}\n",
        "stats_line_correct": "• Верных ответов: {total_correct}\n",
        "stats_line_solved": "• Задач решено: {solved} / {total_questions}\n",
        "stats_line_completion": "• Прогресс: {completion_pct}%\n",
        "stats_line_streak": "• Серия верных подряд: {streak} 🔥\n\n",
        "stats_footer": "Продолжайте практиковаться!",
        "about_title": "ℹ️ <b>О SQLMentor</b>\n\n",
        "about_body": (
            "Небольшой Telegram-бот для интерактивной практики SQL.\n"
            "• 90 отобранных упражнений\n"
            "• 3 уровня сложности\n"
            "• Мгновенная проверка и пояснения\n"
            "• Сохранение прогресса\n\n"
            "Made by <b>APM+ team</b>."
        ),
        "help_full": (
            "ℹ️ <b>Справка SQLMentor</b>\n\n"
            "<b>Команды:</b>\n"
            "/start — Главное меню\n"
            "/help — Эта справка\n\n"
            "<b>Как пользоваться:</b>\n"
            "1. Нажмите <b>📚 Выбрать уровень</b>.\n"
            "2. Выберите тему.\n"
            "3. Прочитайте схему и задание, отправьте SQL.\n"
            "4. Получите ответ, пояснения, переходите дальше.\n"
            "5. <b>📊 Статистика</b> — прогресс в любой момент.\n\n"
            "Советы:\n"
            "• Один запрос — одним сообщением.\n"
            "• Имена таблиц и столбцов как в схеме.\n"
            "• Застряли — кнопка 💡 <b>Подсказка</b>."
        ),
        "topic_complete": (
            "🎉 <b>Тема пройдена!</b>\n\n"
            "Вы дошли до конца этой темы.\n\n"
            "Выберите другую тему или уровень."
        ),
        "hint_intro": "💡 <b>Подсказка</b>\n\n",
        "hint_footer": "\n\nОтправьте ответ SQL обычным текстом.",
        "explain_title": "📖 <b>Пояснение</b>\n\n",
        "correct_answer_label": "<b>Правильный ответ:</b>\n",
        "quiz_intro": (
            "📝 <b>Быстрый тест</b>\n\n"
            "Вопросы с выбором ответа.\n"
            "• Мгновенная проверка\n"
            "• Пояснение к каждому ответу\n\n"
            "Начать?"
        ),
        "quiz_expired": "Сессия теста истекла. Запустите новую.",
        "quiz_complete": (
            "🎉 <b>Тест завершён!</b>\n\n"
            "Счёт: <b>{score} / {total}</b>\n"
            "Точность: <b>{acc}%</b>\n\n"
            "{footer}"
        ),
        "quiz_footer_perfect": "🔥 Отлично!",
        "quiz_footer_good": "💪 Продолжайте!",
        "quiz_footer_low": "📚 Освежите основы и попробуйте снова.",
        "quiz_question_header": "📝 <b>Вопрос {n} из {total}</b>\n\n",
        "quiz_pick_letter": "👆 Нажмите <b>A</b>, <b>B</b>, <b>C</b> или <b>D</b> ниже.",
        "quiz_wrong": "❌ <b>Неверно.</b> Правильный вариант: <b>{label}</b>.",
        "quiz_explain": "📖 <b>Пояснение:</b>\n",
        "quiz_mismatch_alert": "Рассинхрон вопроса. Запустите тест заново.",
        "quiz_expired_alert": "Сессия теста истекла.",
        "need_language": "Нажмите /start и выберите язык.",
        "correct_reply": (
            "✅ <b>Верно!</b>\n\n"
            "Отлично, {name}!\n\n"
            "<b>Ваш ответ:</b>\n<pre>{answer}</pre>"
        ),
        "wrong_reply": (
            "❌ <b>Почти.</b>\n\n"
            "Попробуйте ещё раз.\n\n"
            "<b>Ваш ответ:</b>\n<pre>{answer}</pre>\n\n"
            "Сверьтесь со схемой и синтаксисом."
        ),
        "no_question": "Сначала выберите задачу в меню.",
        "settings_title": "⚙️ <b>Настройки</b>\n\nЯзык:",
        "task_label": "📝 <b>Задание:</b>",
        "schema_label": "🗂️ <b>Схема:</b>",
        "send_sql": "✍️ Отправьте SQL-запрос ответным сообщением.",
        "btn_choose_level": "📚 Выбрать уровень",
        "btn_quiz": "📝 Быстрый тест",
        "btn_stats": "📊 Статистика",
        "btn_about": "ℹ️ О боте",
        "btn_settings": "⚙️ Настройки",
        "btn_back": "⬅️ Назад",
        "btn_home": "🏠 Домой",
        "btn_main_menu": "🏠 Главное меню",
        "btn_hint": "💡 Подсказка",
        "btn_question": "⬅️ К задаче",
        "btn_topics": "⬅️ К темам",
        "btn_next": "➡️ Дальше",
        "btn_retry": "🔄 Ещё раз",
        "btn_explain": "📖 Пояснение",
        "btn_quiz_start": "🚀 Начать тест",
        "btn_quiz_next": "➡️ Следующий вопрос",
        "btn_quiz_end": "🏠 Завершить тест",
        "level_beginner": "🟢 Начинающий",
        "level_intermediate": "🟡 Средний",
        "level_advanced": "🔴 Продвинутый",
    },
}


def tr(lang: str, key: str, **kwargs) -> str:
    loc = lang if lang in STRINGS else "en"
    s = STRINGS[loc].get(key) or STRINGS["en"].get(key, key)
    return s.format(**kwargs) if kwargs else s


def quiz_result_footer(lang: str, score: int, total: int) -> str:
    if total <= 0:
        return tr(lang, "quiz_footer_good")
    if score == total:
        return tr(lang, "quiz_footer_perfect")
    if score >= total / 2:
        return tr(lang, "quiz_footer_good")
    return tr(lang, "quiz_footer_low")
