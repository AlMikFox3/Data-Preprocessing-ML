from csv import reader
from math import sqrt
#loading the csv file
def load_csv(file):
	dataset = list()
	with open(file, 'r') as f:
		csv_data = reader(f)
		for row in csv_data:
			if not row:
				continue
			dataset.append(row)
	return dataset
#converting string values into float
def str_to_float(dataset,col):
	for row in dataset:
		row[col] = (float)(row[col].strip())

#finding the mean for each attribute/column
def find_means(dataset):
	means = [0 for i in range(len(dataset[0]))]
	for col in range(len(dataset[0])):
		colval = [row[col] for row in dataset]
		means[i] = sum(colval)/float(len(dataset))
	return means

#finding the standard deviation of each attribute/column
def find_stdev(dataset, means):
	stdevs = [0 for i in range(len(dataset[0]))]
	for i in range(len(dataset[0])):
		variance = [pow(row[i]-means[i], 2) for row in dataset]
		stdevs[i] = sum(variance)
	stdevs = [sqrt(x/(float(len(dataset)-1))) for x in stdevs]
	return stdevs

#standardizing the dataset
def standardize_data(dataset, means, stdevs):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - means[i]) / stdevs[i]
#writing the normalized data into a new csv file
def write_csv(dataset):
	with open('pima-indians-diabetes-normalized.csv','w') as f:
		for row in dataset:
			for item in row:
				f.write(str(item) + ',')
			f.write('\n')
	f.close()

dataset = load_csv('pima-indians-diabetes.csv')
#print (dataset)
for i in range(len(dataset[0])):
	str_to_float(dataset,i)
#print (dataset)
means = find_means(dataset)
stdevs = find_stdev(dataset, means)
standardize_data(dataset, means, stdevs)
write_csv(dataset)

#Checking mean and std deviation of standardized dataset
new_means = find_means(dataset)
new_stdevs = find_stdev(dataset, new_means)
print('New Means :')
print (new_means)
print('New Std Deviations :')
print (new_stdevs)
