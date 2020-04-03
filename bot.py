# coding=utf-8
# just delet 'your chat id' and add your own and run
#coded by A1ir3z ...

import telebot

bot = telebot.TeleBot("1127879856:AAFyD-v0Td-lgOKQHJM8-X2738cOhK8L0Gc")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hi, send any message you want me to forward to the owner')

@bot.message_handler(func=lambda message: True)
def forward_to_alireza(message):
    send_private_forward(message)


def send_private_forward(message):
    if message != "/start":
        bot.forward_message('your chat id', message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "done! send another message to forward if you want")
    else:
        send_welcome





while True :
    try:
        bot.polling()
    except Exception :
        time.sleep(15)