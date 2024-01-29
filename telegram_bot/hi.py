import telebot
bot = telebot.TeleBot("6262282434:AAEKMMBfPg7opjUKo0dBmNtta9lSbRGLhDc", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['Hello'])
def greet(message):
	bot.reply_to(message, "Hi KF, how are you doing?")

@bot.message_handler(commands=['hi'])
def greet(message):
    chatID = message.chat.id
	# bot.send_message(message.chat.id, "Hi wasuup?")
    bot.send_message(message.chat.id, "Your Group id is {}".format(chatID))


text_options = ['Text 1', 'Text 2']

def send_text():
    print()
    

bot.polling()