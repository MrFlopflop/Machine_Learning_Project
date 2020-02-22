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

for currency in data_dict:
    try:
        print(currency)
        print(data_dict[currency]['2018-10-13'])
    except:
        pass