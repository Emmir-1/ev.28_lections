import telebot 
from telebot import types
import random 


token = "6163743514:AAGt8J0Pdez3l_arNUYh7qL-SwPcYhbfTE0"

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton("Играть")
btn2 = types.KeyboardButton("Нет, я Пас!")
keyboard.add(btn1, btn2)

@bot.message_handler(commands=["start", "game"])
def start_message(massage):
    bot_massage = bot.send_message(massage.chat.id, "Привет Брат!, начнем игру?", reply_markup=keyboard)
    bot.register_next_step_handler(bot_massage, check_answer)

def check_answer(massage):
    if massage.text == "Играть":
        bot.send_message(massage.chat.id, "Окей, тогда лови правила игры:\nНужно угодать число которое я загадаю в диапозоне от 1 до 10 влючительно! у тебя будет 3 попытки! Если ты угодаешь я тебя повешу! ;)")
        number = random.randint(1, 10)
        print(number,"!!!!")
        game(massage, 3, number)
    elif massage.text == "Нет, я Пас!": 
        bot.send_message(massage.chat.id, "Нет так Нет Пока!")
    else:
        bot_massage = bot.send_message(massage.chat.id, "Вы ввели неправельный ответ!\nВведите новый:", reply_markup=keyboard)
        bot.register_next_step_handler(bot_massage, check_answer)

def game(massage, attempts, number):
    massage_bot = bot.send_message(massage.chat.id, "Выбери число:")
    bot.register_next_step_handler(massage_bot, check_number, attempts-1, number)

def check_number(massage, attempts, number):
    if massage.text == str(number):
        bot.send_message(massage.chat.id, "Вы победили! Нарекаю вас удачливым!")
    elif attempts == 0:
        bot.send_message(massage.chat.id,"You\'ve lost again and again!\nBot you\'re still loking at you dream!\nIt\'s not over until you win!")
    else:
        bot.send_message(massage.chat.id, "Нет ты не угодал число, попробуй еще раз!")
        game(massage, attempts, number)
bot.polling()