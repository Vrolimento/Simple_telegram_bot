# -*- coding: utf-8 -*-
import telegram
import time

def main():
    bot = telegram.Bot(token=<token_id>)
    chat_id=<chat_id>
    message='Hi' 
    interval=21000
    while True:
        bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.HTML)
        time.sleep(interval)

if __name__ == '__main__':
    main()






