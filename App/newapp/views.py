from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ChoiceForm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import r2_score
import re

# ML model
file = open('../csv_fake_data.csv', 'r')
df = pd.read_csv(file)
df = df.drop('id', axis=1)
x = df.drop('mental illness', axis=1)
y = df['mental illness']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,
                                                    random_state=101)
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)

model = Sequential()
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')
model.build(x_train.shape)

early_stop = EarlyStopping(monitor='val_loss', patience=2)
model.fit(x=x_train, y=y_train.values, validation_data=(x_test, y_test.values),
          batch_size=128,
          epochs=400,
          callbacks=[early_stop])
file.close()

wordlist = ['anymore', 'hate', 'damn', 'stupid', 'hell', 'sucks', 'kill',
            'annoyed', 'cry', 'grief', 'lonely', 'sad', 'depressed', 'miserable'
    , 'frustrated', 'hurt', 'ugly', 'nasty', 'worried', 'anxious', 'nervous', 'hopeless',
            'hostile', 'ruminate', 'dead', 'kill', 'suicide', 'grave',
            'deceitful', 'pathetic ', 'stupid', 'worthless'
            ]


def contact(request):
    context = {}
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            cat = []
            journal = form.cleaned_data['journal']
            journal = re.split('[,.!() ]', journal)
            while '' in journal:
                journal.remove('')
            score = 0
            for i in journal:
                if i in wordlist:
                    score + 1
            score = score/len(journal)
            score *= 20
            for i in range(1, 10):
                string = 'question' + str(i)
                cat.append(int(form.cleaned_data[string]))
            cat.append(score)
            data = pd.DataFrame(cat)
            data = data.T
            pre = model.predict(data)
            print(pre)
            context['val'] = round(float(pre), 2)
            return render(request, 'newapp/result.html', context)

    form = ChoiceForm()
    return render(request, 'newapp/form.html', {'form': form})



