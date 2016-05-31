from django.shortcuts import render
import pandas as pd
from text_analysis import fileutil
from text_analysis import dbutil

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
	print("nasdaq page")
	path = 'data/nasdaq100list.csv'

	# get csv data from local path
	result = fileutil.get_csv_data(path)

	# insert data to mongodb
	connection = dbutil.get_mongo_connection()
	tbl = dbutil.get_mongo_connection(connection)
	# tbl.insert_bulk_data()

	print(result)
	return render(request, 'nasdaq.html', context={'result':result})

def nasdaq_viz_page(request):
	return render(request, 'nasdaq_viz.html')
