from telebot import *
from db import Db
from gen import Generator
from sql import Sql
from rnd import Rnd
import json
import sqlite3


with open('credentials.json') as f:
	data = json.load(f)

bot = TeleBot(data['token'])

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