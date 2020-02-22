from sklearn.linear_model import SGDClassifier

x = [[0., 0., 0.], [1., 0., 2.], [1., 1., 2.], [2., -1., 2.]]
y = [0, 0, 1, -1]
clf = SGDClassifier(loss='hinge', penalty='l2', max_iter=5)
clf.fit(x, y)
SGDClassifier(max_iter=5)

print(clf.predict([[1., -1., 0.]]))
print(clf.coef_)
print(clf.intercept_)
print(clf.decision_function([[1., -1., 0.]]))

# 1: Make a dict with the right features for each date
# 2: Make a function that can take this dict and append the features of the previous 30 dates
# to the x and y lists (we will have to exclude 30 dates per currency which is a total of 8070
# dates but that still leaves us with (at least) 374,827 dates (aka samples) in total)
# 3: Split up the x and y lists into a training set and a test set
