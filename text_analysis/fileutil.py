import pandas as pd

def read_localcsv(path):
	result = pd.read_csv(path, encoding='UTF-8')
	print(result)
	return result