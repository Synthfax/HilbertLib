from hilbertlib.bot_development.telegram_bot import TelegramBot

bot = TelegramBot("BOT_TOKEN_HERE")

bot.add_command("hi", "Hey there!") # /hi command
bot.add_trigger("hello", "Hi! How can I help you?") # respond with "Hi! How can I help you" when user sent "hello"

bot.run()