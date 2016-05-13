import pandas as pd
import csv
import json

def read_localcsv(path):
	result = pd.read_csv(path, encoding='UTF-8')
	print(result)
	return result

def get_data(path):
    #r = requests.get(URL)
    #data = r.text
	RESULTS = {"children": []}
	with open(path) as csvfile:
		reader = csv.DictReader(csvfile)
		for line in reader:
			RESULTS['children'].append({
			"name": line['Name'],
			"symbol": line['Symbol'],
			"symbol": line['Symbol'],
			"price": line['lastsale'],
			"net_change": line['netchange'],
			"percent_change": line['pctchange'],
			"volume": line['share_volume'],
			"value": line['Nasdaq100_points']
			})
	#print(json.dumps(RESULTS))
	return json.dumps(RESULTS)
