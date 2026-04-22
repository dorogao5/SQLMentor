import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters

from bot.config import TELEGRAM_BOT_TOKEN, logger
from bot.database import init_db
from bot.handlers import start_command, help_command, menu_callback, handle_message, error_handler


async def post_init(application: Application):
    await init_db()


def main():
    logger.info("Starting SQLMentor bot...")

    db_dir = os.path.dirname(os.path.abspath("data/sqlmentor.db"))
    os.makedirs(db_dir, exist_ok=True)

    application = (
        Application.builder()
        .token(TELEGRAM_BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(menu_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_error_handler(error_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
