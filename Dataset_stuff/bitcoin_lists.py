import datetime
from make_dict import data_dict
from random import randint

x = []
y = []

for date in data_dict['Bitcoin']:
    sample = data_dict['Bitcoin'][date]
    features = [float(sample['open'])]
    try:
        for i in range(1, 30):
            prev_date = str(datetime.date(*map(int, date.split('-')))-datetime.timedelta(i))
            prev = data_dict['Bitcoin'][prev_date]
            features.append(float(prev['open']))
            features.append(float(prev['close']))
            features.append(float(prev['high']))
            features.append(float(prev['low']))
            features.append(float(prev['volume']))
            features.append(float(prev['market']))
        x.append(features)
        y.append(sample['class'])
    except:
        pass

test = [[], []]
for i in range(0, 100):
    sample_i = randint(0, len(y)-1)
    test[0].append(x.pop(sample_i))
    test[1].append(y.pop(sample_i))
