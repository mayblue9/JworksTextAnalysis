from django.shortcuts import render
import pandas as pd
from text_analysis import fileutil

# Create your views here.
def home_page(request, pid):
	print("Hello World")

	# read csv from local
	result = fileutil.read_localcsv('data/livetalk.csv')

	return render(request, 'home.html', context={'data':"hello world!",})

def viz_page(request):
	print("Viz display")

	return render(request, 'viz.html')