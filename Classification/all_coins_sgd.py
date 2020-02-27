from sklearn.linear_model import SGDClassifier
from sklearn.kernel_approximation import RBFSampler
from all_coins_lists import x, y, test

rbf_feature = RBFSampler(gamma=1, n_components=len(x[0]))
X_features = rbf_feature.fit_transform(x)

clf = SGDClassifier(max_iter=1000)
clf.fit(X_features, y)
SGDClassifier(max_iter=1000)

pred = clf.predict(test[0])
for i in range(0, 100):
    print('Predicted Class: ' + pred[i] + ' | Actual Class: ' + test[1][i])