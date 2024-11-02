import telebot
from telebot.types import Message
import random
import os
a = random.randint(0,1000)
bot = telebot.TeleBot('7965011811:AAFlXPBXM1A7jVP5R16M3Y7Wupj5oFMlCrU')


@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.reply_to(message, 'Привет!👋')


@bot.message_handler(commands=['name'])
def cmd_name(message:Message):
    bot.reply_to(message, 'Меня зовут Мистер Экономик🌍')


@bot.message_handler(commands=['mem'])
def cmd_mem(message:Message):
    pictures = os.listdir('meme')
    with open('meme/' +  random.choice (pictures),'rb') as file:
        bot.send_photo(message.chat.id , file)


@bot.message_handler(commands=['help'])
def cmd_help(message:Message):
    bot.reply_to(message, 'mem - отправить случайный мемчик,info-инфа о боте,name - узнать имя бота,start - начать работу бота,plastic-инфа о вреде пластика,polietelen-вред полителена,metal-вред металла,bye-прощание')


@bot.message_handler(commands=['info'])
def cmd_info(message:Message):
    bot.reply_to(message,'Мистер Экономик создан для того чтобы подростки задумались и перестали зассорять нашу планету😁')


@bot.message_handler(commands=['plastic'])
def cmd_info(message:Message):
    bot.reply_to(message,'Человек получает много плохих веществ и микропластика на протяжении жизни через вдыхание, проглатывание и прикосновения с кожей🚫.')
    pictures = os.listdir('meme')
    with open('meme/' +  random.choice (pictures),'rb') as file:
        bot.send_photo(message.chat.id , file)



@bot.message_handler(commands=['polietelen'])
def cmd_info(message:Message):
    bot.reply_to(message,'Входящие в его состав вещества плохо влияют на печень.')
    pictures = os.listdir('meme')
    with open('meme/' +  random.choice (pictures),'rb') as file:
        bot.send_photo(message.chat.id , file)


@bot.message_handler(commands=['metal'])
def cmd_info(message:Message):
    bot.reply_to(message,'Загрязнение земли и воды металлами снижает активное действие почвы, ухудшает качество вод и плохо влияет на экосистемы в воде.')
    pictures = os.listdir('meme')
    with open('meme/' +  random.choice (pictures),'rb') as file:
        bot.send_photo(message.chat.id , file)



@bot.message_handler(commands=['bye'])
def cmd_info(message:Message):
    bot.reply_to(message,'Пока и не сори😉🚯')
    pictures = os.listdir('meme')
    with open('meme/' +  random.choice (pictures),'rb') as file:
        bot.send_photo(message.chat.id , file)

    









bot.polling()
