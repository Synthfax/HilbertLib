from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.commands = {}
        self.triggers = {}
        self.user_ids = set()
        self._app = None

    def add_command(self, command: str, response: str):
        self.commands[command] = response

    def add_trigger(self, user_message: str, bot_response: str):
        self.triggers[user_message.lower()] = bot_response

    async def _handle_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        command = update.message.text.lstrip('/').split()[0]

        if command in self.commands:
            await update.message.reply_text(self.commands[command])
        else:
            await update.message.reply_text("Unknown command.")

    async def _handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_msg = update.message.text.strip().lower()
        self.user_ids.add(update.effective_user.id)

        if user_msg in self.triggers:
            await update.message.reply_text(self.triggers[user_msg])

    def run(self):
        app = ApplicationBuilder().token(self.token).build()
        self._app = app

        for command_name in self.commands:
            app.add_handler(CommandHandler(command_name, self._handle_command))

        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self._handle_message))

        print("Bot is running...")
        app.run_polling()
