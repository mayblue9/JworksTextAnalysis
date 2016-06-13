from django.shortcuts import render
import pandas as pd
from text_analysis import fileutil
from text_analysis import dbutil
import csv
from konlpy.tag import Hannanum
from collections import Counter

# Create your views here.
def home_page(request, pid):
	print("Hello World")

	# read csv from local
	result = fileutil.read_localcsv('data/livetalk.csv')

	return render(request, 'home.html', context={'data':"hello world!",})

def viz_page(request):
	print("Viz display")

	return render(request, 'viz.html')

def nasdaq_page(request):

	path = 'data/livetalk.csv'

	# get csv data from local path
	with open(path) as csvfile:
		reader = csv.DictReader(csvfile)
		content = ''
		for line in reader:
			content += ' ' + line['BLTTHG_CNTNT']

		# initiate Hannanum instance
		h = Hannanum()
		nouns = h.nouns(content)
		c = Counter(nouns)

	# insert data to mongodb
	# connection = dbutil.get_mongo_connection()
	# tbl = dbutil.get_mongo_connection(connection)

	# tbl.insert_bulk_data()
	# dbutil.insert_text_analysis_data(tbl,c)

	# return render(request, 'nasdaq.html', context={'result':csv_data})
	return render(request, 'nasdaq.html')

def nasdaq_viz_page(request):
	return render(request, 'nasdaq_viz.html')

# view for d3example
def d3_example_page(request):
	return render(request, 'd3example.html')
