import datetime
import pandas as pd
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.preprocessing.sequence import TimeseriesGenerator

PATH = 'ml\cost_prediction\BTC_ALL_graph_coinmarketcap.csv'
data = pd.read_csv(PATH, sep=';')

def getData(PATH, data):
    def getUnix(s):

        s = s.split('T')
        date = [int(i) for i in s[0].split('-')]
        t = [int(i) for i in s[1].split('.')[:-1][0].split(':')]

        return int(time.mktime(datetime.datetime(*date).timetuple()))

    newTime = []
    for i in data['timestamp'].values:
        newTime.append(getUnix(i))

    newTime = np.array(newTime)
    data['timestamp'] = newTime
    print(data)

    data = np.array(data)


    xLen = 50                      #Анализируем по 300 прошедшим точкам    731x6
    valLen = 200                  #Используем 30.000 записей для проверки

    trainLen = data.shape[0]-valLen # 631

    #Делим данные на тренировочную и тестовую выборки 
    xTrain, xTest = data[:trainLen], data[trainLen+2+xLen:]

    #Масштабируем данные (отдельно для X и Y), чтобы их легче было скормить сетке
    xScaler = MinMaxScaler()
    xScaler.fit(xTrain)
    xTrain = xScaler.transform(xTrain)
    print(xTrain)
    xTest = xScaler.transform(xTest)

    #Делаем reshape,т.к. у нас только один столбец по одному значению
    yTrain, yTest = np.reshape(data[:trainLen,3],(-1,1)), np.reshape(data[trainLen+xLen+2:,3],(-1,1)) 
    yScaler = MinMaxScaler()
    yScaler.fit(yTrain)
    yTrain = yScaler.transform(yTrain)
    yTest = yScaler.transform(yTest)

    #Создаем генератор для обучения
    trainDataGen = TimeseriesGenerator(xTrain, yTrain,           #В качестве параметров наши выборки
                                length=xLen, stride=1, sampling_rate=1, #Для каждой точки (из промежутка длины xLen)
                                batch_size=20)                #Размер batch, который будем скармливать модели

    #Создаем аналогичный генератор для валидации при обучении
    testDataGen = TimeseriesGenerator(xTest, yTest,
                                length=xLen, stride=1,
                                batch_size=20)
    print(trainDataGen[0][0].shape,
        trainDataGen[0][1].shape)
    
    return xTrain, yTrain, xTest, yTest, xLen, trainDataGen, testDataGen, yScaler
