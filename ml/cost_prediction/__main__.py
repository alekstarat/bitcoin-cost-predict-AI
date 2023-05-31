import pandas as pd #Пандас
import matplotlib.pyplot as plt #Отрисовка графиков
from keras.utils import to_categorical 
import numpy as np #Numpy
from keras.optimizers import Adam #Оптимизатор
from keras.models import Sequential, Model #Два варианты моделей
from keras.layers import concatenate, Input, Dense, Dropout, BatchNormalization, Flatten, Conv1D, Conv2D, LSTM, GlobalMaxPooling1D, MaxPooling1D, RepeatVector #Стандартные слои
from sklearn.preprocessing import StandardScaler, MinMaxScaler #Нормировщики
from keras.preprocessing.sequence import TimeseriesGenerator
from dataset import *
from visual import *

def getPred(currModel, xVal, yVal, yScaler):

  predVal = yScaler.inverse_transform(currModel.predict(xVal))
  yValUnscaled = yScaler.inverse_transform(yVal)
  
  return (predVal, yValUnscaled)


PATH = 'ml\cost_prediction\BTC_ALL_graph_coinmarketcap.csv'
data = pd.read_csv(PATH, sep=';')


xTrain, yTrain, xTest, yTest, xLen, trainDataGen, testDataGen, yScaler = getData(PATH=PATH, data=data)

DataGen = TimeseriesGenerator(xTest, yTest,
                               length=50, sampling_rate=1,
                               batch_size=len(xTest)) 
xVal = []
yVal = []
for i in DataGen:
  xVal.append(i[0])
  yVal.append(i[1])

xVal = np.array(xVal)
yVal = np.array(yVal)


modelD = Sequential()
modelD.add(Dense(150,input_shape = (xLen,7), activation="relu" )) 
modelD.add(Flatten())
modelD.add(Dense(1, activation="linear"))


modelD.compile(loss="mse", optimizer=Adam(lr=1e-4))

modelD.summary()

history = modelD.fit(
                    trainDataGen, 
                    epochs=50, 
                    verbose=1, 
                    validation_data = testDataGen 
                    )

currModel = modelD 
(predVal, yValUnscaled) = getPred(currModel, xVal[0], yVal[0], yScaler) 
print(predVal)

showPredict(0, 160, 0, predVal, yValUnscaled)