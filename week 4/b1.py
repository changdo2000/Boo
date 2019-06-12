import pandas as pd 
import numpy as np 

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC


def main():
	data = pd.read_csv("data.csv")
	x = np.array(data.iloc[:, 0:2])
	y = np.array(data.iloc[:, 2])
	leuleu_1 = LogisticRegression()
	leuleu_2 = RandomForestClassifier()
	leuleu_3 = LinearSVC()
	train_samples = 60
	x_train = x[:train_samples]
	x_test = x[train_samples:]
	y_train = y[:train_samples]
	y_test = y[train_samples:]
	dem = 0
	leuleu_1.fit(x_train, y_train)
	for i in range(len(x_test)):
		if leuleu_1.predict([x_test[i]]) == y_test[i]:
			dem += 1
	accuracy_1 = dem / len(y_test)
	dem = 0
	leuleu_2.fit(x_train, y_train)
	for i in range(len(x_test)):
		if leuleu_2.predict([x_test[i]]) == y_test[i]:
			dem += 1
	accuracy_2 = dem / len(y_test)
	dem = 0
	leuleu_3.fit(x_train, y_train)
	for i in range(len(x_test)):
		if leuleu_3.predict([x_test[i]]) == y_test[i]:
			dem += 1
	accuracy_3 = dem / len(y_test)
	print (accuracy_1)
	print (accuracy_2)
	print (accuracy_3)

if __name__ == '__main__':
	main()