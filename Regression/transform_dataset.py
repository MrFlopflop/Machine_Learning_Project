currencies = []

with open('currencies.txt', 'r') as f:
    line = f.readline()
    while line:
        currencies.append(line[:-1])
        line = f.readline()

print(currencies)

observations = 0
buy = 0
sell = 0
stay = 0

with open('transformed_dataset.csv', 'w') as outfile, open('crypto-markets.csv', 'r') as infile:
    outfile.write('name,date,open,close,high,low,volume,market,class\n')
    line = infile.readline()
    line = infile.readline()
    while line:
        line = line.split(',')
        name = line[2]
        date = line[3]
        open = line[5]
        close = line[8]
        high = line[6]
        low = line[7]
        volume = line[9]
        market = line[10]
        # Excludes all currencies that do not have at least 1000 observations
        # And all observations where the volume is 0 since this is missing data (should be discussed in report)
        if name in currencies and volume != '0':
            observations += 1
            # If the value goes up by at least 2.5%
            if float(close) > float(open) + 0.025*float(open):
                clss = 'BUY'
                buy += 1
            # If the value goes down by at least 2.5%
            elif float(close) < float(open) - 0.025*float(open):
                clss = 'SELL'
                sell += 1
            else:
                clss = 'STAY'
                stay += 1
            # We should have a look at these classifiers, maybe make them scale with the value

            outline = name + ',' + date + ',' + open + ',' + close + ',' + high + ',' + low + ',' + \
                      volume + ',' + market + ',' + clss + '\n'
            outfile.write(outline)
        line = infile.readline()

# Prints the total amount of observations in the transformed dataset
# and the amount of observations that were classified as BUY, SELL, and STAY respectively
print('Observations: ' + str(observations))
print('BUY: ' + str(buy))
print('SELL: ' + str(sell))
print('STAY: ' + str(stay))
