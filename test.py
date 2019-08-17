import csv

train_reader = csv.reader(open("data/test.csv", 'r'), delimiter=",")

train_data = []
train_target = []

for row in train_reader:
	train_data.append([row[0], row[1], row[2], row[3], row[4]])	
							

	train_target.append(row[0])

print(train_data)