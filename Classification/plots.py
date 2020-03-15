import matplotlib.pyplot as plt
from make_dict import data_dict
from datetime import datetime
from random import randint

coinlist =[]

with open('../Regression/currencies.txt', 'r') as file:
    all_coins = file.readlines()
    for i in range(0, 4):
        x = randint(0, len(all_coins))
        coinlist.append(all_coins[x][:-1])

for coin in coinlist:
    values = []
    dates = []
    counter = 0
    for date in data_dict[coin]:
        if (int(date[0:4]) == 2017 and int(date[5:7]) >= 6) or int(date[0:4]) > 2017:
            counter += 1
            if counter == 5:
                dates.append(datetime.strptime(date, '%Y-%m-%d'))
                open = float(data_dict[coin][date]['open'])
                close = float(data_dict[coin][date]['close'])
                diff = open - close
                values.append(diff)
                counter = 0
    plt.plot(dates, values, label=coin)

plt.legend(loc=2)
plt.title('Difference in open and close prices every 5 days')

plt.savefig('Plot.png')
plt.show()