from sklearn.linear_model import SGDClassifier
from bitcoin_lists import x, y, test

clf = SGDClassifier(loss='hinge', penalty='l2', max_iter=1000)
clf.fit(x, y)
SGDClassifier(max_iter=1000)

pred = clf.predict(test[0])
for i in range(0, 100):
    print('Predicted Class: ' + pred[i] + ' | Actual Class: ' + test[1][i])