from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
from all_coins_lists import x as X_Train, y as Y_Train, test


def difference (a, b):
    return abs(1 - b/a)*100

scaler = StandardScaler()
scaler.fit(X_Train)
X_Train = scaler.transform(X_Train)
X_Test = scaler.transform(test[0])

clf = SGDRegressor(max_iter=1000, loss='huber', epsilon=0.2)
clf.fit(X_Train, Y_Train)
SGDRegressor(max_iter=1000)

pred = clf.predict(X_Test)
for i in range(0, len(pred)):
    print('Predicted Value: ' + str(abs(pred[i])) + ' | Actual Value: ' + str(test[1][i]))
    print('Difference: ' + str("%.2f" % difference(float(test[1][i]), abs(float(pred[i])))) + '%')
