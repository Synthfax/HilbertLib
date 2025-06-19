from hilbertlib.bot_development.chatbot import ChatBot

bot = ChatBot()

bot.load('my_hlibcb_model.hlibcb')

while True:
    prompt = input("> ")
    print(bot.get_response(prompt.lower))