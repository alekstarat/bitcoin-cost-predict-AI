import telebot
import requests
import pandas as pd
import json
import os

bot = telebot.TeleBot('5063930255:AAFXg8x-DiyW_dZc5r3SqQU9JNc8_TuxkrM')
URL = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/detail/chart?id=1&range=1D'

def prepare_graph(data : dict, timestamp : str):

    close = []
    volume = []
    cap = []
    for i in data:
        try:
            close.append(i['c'][0])
            volume.append(i['c'][1])
            cap.append(i['c'][2])
        except:
            pass
    units = len(close)
    currDF = pd.DataFrame(columns = ['close', 'volume', 'marketCap', 'timestamp'])
    currDF['close'] = close
    currDF['volume'] = volume
    currDF['marketCap'] = cap
    currDF['timestamp'] = [timestamp]*units

    print(currDF)
    return currDF

@bot.message_handler(commands=['start'])
def welcome(message):

    a = json.loads(requests.get(URL).text)
    global timestamp
    timestamp = a['status']['timestamp']

    data = a['data']['points'].values()
    #print(a)
    bot.send_message(message.from_user.id, a)
    global currDF
    currDF = prepare_graph(data, timestamp)
    bot.send_message(message.chat.id, str(currDF))

@bot.message_handler(commands=['save_day'])
def save_day(message):
    name = timestamp.split('T')[0]
    if not(f'{name}.xlsx' in os.listdir('ml\cost_prediction\database_bot\days_xlsx')):
        currDF.to_excel(f'ml\cost_prediction\database_bot\days_xlsx\{name}.xlsx')
        bot.send_message(message.chat.id, 'Сохранено!')
    else:
        bot.send_message(message.chat.id, 'Файл уже сохранён')


bot.polling(non_stop=True)