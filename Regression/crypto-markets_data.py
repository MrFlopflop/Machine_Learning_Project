# For exploring the dataset, feel free to change some code

currencies = {}
total_observations = 0
with open('crypto-markets.csv', 'r') as file:
    line = file.readline()
    line = file.readline()
    while line:
        total_observations += 1
        line = line.split(',')
        name = line[2]
        if name not in currencies:
            currencies[name] = 1
        else:
            currencies[name] += 1
        line = file.readline()

observations = 0

f = open('currencies.txt', 'w')
for coin in currencies:
    if currencies[coin] >= 1000:
        print(coin + ' : ' + str(currencies[coin]))
        observations += currencies[coin]
        f.write(coin+'\n')

print('Observations with at least 1000 per coin: ' + str(observations))
print('Total observations in dataset: ' + str(total_observations))

# Relevant features might be: open, close, high, low, volume, market

# Lets say we want to be able to predict whether the price is gonna go up today (close > open),
# the price is gonna go down today (close < open), or if it will stay the same (close = open).
# And we look at the relevant features of the previous 30 days to try to predict that.
# We could classify the options as BUY, STAY, and SELL
# Then we would have to transform this dataset so it only contains the relevant features and a class
