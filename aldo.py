from telebot import *
from db import Db
from gen import Generator
from sql import Sql
from rnd import Rnd
import sqlite3

bot = TeleBot("487462699:AAFqHxeyFzA3BynQ6XGgFGwzlfgUGiQK7Q4")

@bot.message_handler(func=lambda message: True)
def improvise(message):
	print(" >>> " + message.from_user.first_name + " : " + message.text)
	if "📝" in message.text:
		db = Db(sqlite3.connect('booba.db'), Sql())
		generator = Generator('booba', db, Rnd())
		msg = generator.generate(' ') + "\n" + generator.generate(' ')
		bot.send_message(message.chat.id, msg)

print(" > Aldo is now up and running!")
bot.polling()