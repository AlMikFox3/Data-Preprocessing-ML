from csv import reader
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
#finding the minimum and maximum values for each attribute/column
def find_minmax(dataset):
	minmax = list()
	for col in range(len(dataset[0])):
		colval = [row[col] for row in dataset]
		min_val = min(colval)
		max_val = max(colval)
		minmax.append([min_val,max_val])
	return minmax 
#normalizing the dataset
def normalize_data(dataset, minmax):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i]-minmax[i][0])/(minmax[i][1]-minmax[i][0])
#writing the normalized data into a new csv file
def write_csv(dataset):
	with open('pima-indians-diabetes-normalized.csv','w') as f:
		for row in dataset:
			for item in row:
				f.write(str(item) + ',')
			f.write('\n')

dataset = load_csv('pima-indians-diabetes.csv')
#print (dataset)
for i in range(len(dataset[0])):
	str_to_float(dataset,i)
#print (dataset)
minmax = find_minmax(dataset)
#print (minmax)
normalize_data(dataset, minmax)
#print (dataset[:30])
#write the normalized dataset into a csv file
write_csv(dataset)
