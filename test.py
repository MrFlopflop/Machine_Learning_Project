import numpy as np
import sklearn
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset, and select one feature (Body Mass Index)
x, y = datasets.load_diabetes(True)
x = x[:, 2].reshape(-1, 1)

# -- the reshape operation ensures that x still has two dimensions 
# (that is, we need it to be an n by 1 matrix, not a vector)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5)

plt.scatter(x_train[:, 0], y_train)

plt.xlabel('BMI')
plt.ylabel('disease progression');
plt.show()