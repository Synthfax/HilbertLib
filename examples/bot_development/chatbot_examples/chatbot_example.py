from hilbertlib.bot_development.chatbot import ChatBot

bot = ChatBot()

bot.add("hello", "Hi there!")
bot.add("how are you", "Im good!", 80)

bot.save("my_hlibcb_model")

while True:
    prompt = input("> ")
    print(bot.get_response(prompt.lower))