import datetime
import telebot;
import cv2;
import config
import telebot
from telebot import apihelper
from telebot import types
import datetime
import os

bot = telebot.TeleBot(config.TOKEN)

def autor(chatid):
    strid = str(chatid)
    for item in config.ADMINS:
        if item == strid:
            return True
    return False

def main():
    bot.send_message(config.ADMIN, "START BOT")

@bot.message_handler(commands=['start'])
def handle_start(message):
    start_keybord = telebot.types.ReplyKeyboardMarkup()
    start_keybord.row('Погнали','Статистика участников','Топ жоп')
    bot.send_message(message.from_user.id, "Доброго пожаловать на атракион невиданной щедрости\r\n Попробуй угадать чья жопа перед тобой", reply_markup=start_keybord)

# @bot.message_handler(content_types=['text'])
# def handle_text(message):

if __name__ == '__main__':
    bot.polling(none_stop=True)