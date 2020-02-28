# -*- coding: utf-8 -*-
import telebot
import pyautogui
import os
import time


###BOT API###
bot = telebot.TeleBot("")
###BOT API###

#Выберете язык вашей системы [1]Ru [2]En Select language your system
language = 1

if language == 1:#РУССКИЙ
    #Пожалуйста введите имя пользователя в переменную user name для того чтобы знать через какую директорию загружать файл:
  #####################
  ###               ###
  ##                 ##
    username = 'root'
  ##                 ##
  ###               ###
  #####################
    if username == 'root':
        folder = "/root/Изображения/aircrackscreen/file.jpg"
    else:
        folder = '/home/' + username + '/Изображения/aircrackscreen/file.jpg'
    
    picture = "Изображения"
    #print("Окей вот он русский ;)")

    reply = "Пожалуйста выполните комманду в линукс терминале [aircrack-ng file.cap -w wordlist.txt && python3 index.py] объясняю после того как словарь перебереться тогда сделается скриншот и отпрвиться к вашему телеграмм боту"
elif language == 2:#ENGLISH
    #Please enter a username for variable 'username' in order to know through which directory to upload the file:
    
  #####################
  ###               ###
  ##                 ##
    username = 'root'
  ##                 ##
  ###               ###
  #####################


    if username == 'root':
        folder = "/root/Picture/aircrackscreen/file.jpg"
    else:
        folder = '/home/' + username + '/Picture/aircrackscreen/file.jpg'


    picture = "Picture"
    reply = "Please send a command to Linux terminal [aircrack-ng file.cap -w wordlist.txt && python3 index.py] explanation: after the dictionary is scanned then a screenshot is created and sent to your telegram bot (translated by google translator)"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, reply)
@bot.message_handler(content_types=['photo', 'text'])
def send_message(message):
    #bot.send_message(message.chat.id, message.text)
    if message.text == "/photo":
        os.system("rm -rf ~/" + picture + "/*")
        os.system("mkdir ~/" + picture + "/aircrackscreen")
        for i in range(1):
            pyautogui.press('printscreen')#screenshot
            time.sleep(2)
        os.system("convert ~/" + picture + "/*.png ~/" + picture + "/aircrackscreen/file.jpg")
        time.sleep(3)
        
        image = open(folder, 'rb')
        bot.send_photo(message.chat.id, image)#send photo file
        image.close()#close file



bot.polling( none_stop = True)
