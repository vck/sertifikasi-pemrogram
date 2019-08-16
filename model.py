import numpy as np 
from sklearn.linear_model import LogisticRegression
import csv 

class Credito:
	def __init__(self, train_dir, test_dir, max_iter=100):
		"""
		train: direktori data train
		test: direktori data test
		"""
		self.train_dir = train_dir
		self.test_dir = test_dir
		self.train_data = []
		self.train_target = []
		self.test_data = [] 
		self.test_target = []

	def preprocessing(self):
		"""
		return: None
		"""
		train_reader = csv.DictReader(open(self.train_dir, 'r'), delimiter=",")
		for row in train_reader:
			self.train_data.append([row["BUSAGE"],
									row["BUSTYPE"],	
									row["BUSAGE"],
									row["MAXLINEUTIL"],
									row["DAYSDELQ"],
									row["TOTACBAL"]]	
								)

			self.train_target.append([row["DEFAULT"]])

		train_reader = csv.DictReader(open(self.test_dir, 'r'), delimiter=",")
		for row in train_reader:
			self.test_data.append([row["BUSAGE"],
									row["BUSTYPE"],	
									row["BUSAGE"],
									row["MAXLINEUTIL"],
									row["DAYSDELQ"],
									row["TOTACBAL"]]	
								)

			self.test_target.append([row["DEFAULT"]])

		# convert data to numpy array
		self.train_data = np.array(self.train_data)
		self.test_data = np.array(self.test_data)

		# convert target to numpy array
		self.train_target = np.array(self.train_target)
		self.test_target = np.array(self.test_target)

		assert len(self.test_target) == len(self.test_data)

	def train(self, max_iter=100):
		"""
		params:
		max_iter -> banyak iterasi:int
		"""
		self.model = LogisticRegression(max_iter=max_iter)
		self.train.fit()

if __name__ == '__main__':
	test_dir = "data/test.csv"
	train_dir = "data/train.csv"

	credito = Credito(train_dir, test_dir, max_iter=1000)
	credito.preprocessing()