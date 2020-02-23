data_dict = {}

with open('transformed_dataset.csv', 'r') as file:
    line = file.readline()
    line = file.readline()
    while line:
        line = line.split(',')
        name = line[0]
        date = line[1]
        open = line[2]
        close = line[3]
        high = line[4]
        low = line[5]
        volume = line[6]
        market = line[7]
        clss = line[8][:-1]

        if name not in data_dict:
            data_dict[name] = {}

        sample = {
            'class': clss,
            'open': open,
            'close': close,
            'high': high,
            'low': low,
            'volume': volume,
            'market': market,
        }

        data_dict[name][date] = sample

        line = file.readline()

# ----Testing stuff----

sell = 0
buy = 0
stay = 0

for date in data_dict['Bitcoin']:
    # print(data_dict['Bitcoin'][date])
    clss = data_dict['Bitcoin'][date]['class']
    if clss == 'BUY':
        buy += 1
    elif clss == 'SELL':
        sell += 1
    else:
        stay += 1

# print('BUY: ' + str(buy))
# print('SELL: ' + str(sell))
# print('STAY: ' + str(stay))