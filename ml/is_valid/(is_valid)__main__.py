# Для работы с файлами 
import numpy as np # Для работы с данными 
import pandas as pd # Для работы с таблицами
import matplotlib.pyplot as plt # Для вывода графиков
import os # Для работы с файлами
import pandas as pd

from keras import utils # Для работы с категориальными данными
from keras.models import Sequential # Полносвязная модель
from keras.optimizers import Adam
from keras.layers import Dense, Dropout, SpatialDropout1D, BatchNormalization, Embedding, Flatten, Activation # Слои для сети
from keras.preprocessing.text import Tokenizer # Методы для работы с текстами и преобразования их в последовательности

from sklearn.preprocessing import LabelEncoder # Метод кодирования тестовых лейблов
from sklearn.model_selection import train_test_split


df = pd.read_excel('ml\is_valid\output.xlsx')
x_train = np.array(df['data'])
y_train = np.array(df['is_valid'])
y_train = utils.to_categorical(y_train, 2)


maxWordsCount = 15

tokenizer = Tokenizer(num_words=maxWordsCount, filters='–—!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n\xa0–\ufeff', lower=True, split=' ', char_level=False, oov_token = 'unknown')
tokenizer.fit_on_texts(x_train)
items = list(tokenizer.word_index.keys())
trainIndx = tokenizer.texts_to_sequences(x_train)


def getSetFromIndexes(wordIndexes, xLen, step):
  xSample = []
  wordsLen = len(wordIndexes)
  index = 0
  
  # Идём по всей длине вектора индексов
  # "Откусываем" векторы длины xLen и смещаеммся вперёд на step
  
  while (index + xLen <= wordsLen):
    xSample.append(wordIndexes[index:index+xLen])
    index += step
    
  return xSample

def createSetsMultiClasses(wordIndexes, xLen, step): # функция принимает последовательность индексов, размер окна, шаг окна

  # Для каждого из 6 классов
  # Создаём обучающую/проверочную выборку из индексов
  nClasses = len(wordIndexes) # задаем количество классов выборки
  classesXSamples = []        # здесь будет список размером "кол-во классов*кол-во окон в тексте*длину окна(например 6 по 1341*1000)"
  for wI in wordIndexes:      # для каждого текста выборки из последовательности индексов
    classesXSamples.append(getSetFromIndexes(wI, xLen, step)) # добавляем в список очередной текст индексов, разбитый на "кол-во окон*длину окна" 

  # Формируем один общий xSamples
  xSamples = [] # здесь будет список размером "суммарное кол-во окон во всех текстах*длину окна(например 15779*1000)"
  
  for t in range(nClasses):  # в диапазоне кол-ва классов(6)
    xT = classesXSamples[t]  # берем очередной текст вида "кол-во окон в тексте*длину окна"(например 1341*1000)
    for i in range(len(xT)): # и каждое его окно
      xSamples.append(xT[i]) # добавляем в общий список выборки

  xSamples = np.array(xSamples) # переводим в массив numpy для подачи в нейронку
  
  
  return xSamples

X_train = createSetsMultiClasses(trainIndx, 2, 40)
print(y_train.shape)
print(X_train.shape)

model03 = Sequential()
model03.add(Embedding(maxWordsCount, 20, input_length=2))
model03.add(SpatialDropout1D(0.2))
model03.add(Flatten())
model03.add(BatchNormalization())
model03.add(Dense(200, activation="relu"))
model03.add(Dropout(0.2))
model03.add(BatchNormalization())
model03.add(Dense(2, activation='softmax'))

model03.compile(optimizer='adam', 
              loss='binary_crossentropy', 
              metrics=['accuracy'])

model03.fit(X_train, y_train, epochs=100, verbose=1)

n = 18

a = model03.predict(X_train)[n]
print(np.argmax(a))
print(np.argmax(y_train[n]))