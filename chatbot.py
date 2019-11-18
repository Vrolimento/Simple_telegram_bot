# -*- coding: utf-8 -*-
import telegram
import time

def main():
    bot = telegram.Bot(token=<864236860:AAHffJJoFjbfJ6HyAr3b_YmOzASY5oXvecY>)
    chat_id=<chat_id>
    message='Hi, i am a new bot of TELEGRAM. I am will post message every 60 sec. Good Bye!' 
    interval=60
    while True:
        bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.HTML)
        time.sleep(interval)

if __name__ == '__main__':
    main()






