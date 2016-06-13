from konlpy.tag import Hannanum
from collections import Counter
import pandas as pd
import csv
import json

def read_localcsv(path):
	result = pd.read_csv(path, encoding='UTF-8')
	print(result)
	return result

def get_json_data(path):
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
	# print(json.dumps(RESULTS))

	return json.dumps(RESULTS)

def get_tags(text, ntags=50, multiplier=10):
	h = Hannanum()
	nouns = h.nouns(text)
	count = Counter(nouns)

	# for word,cnt in count.most_common(ntags):
	#	print(word,cnt)
	return count

def get_csv_data(path, column):
	# localcsv = read_localcsv(path)
	with open(path) as csvfile:
		reader = csv.DictReader(csvfile)
		content = ''
		for line in reader:
			content += ' ' + line[column]
		tags = get_tags(content)

	return tags
