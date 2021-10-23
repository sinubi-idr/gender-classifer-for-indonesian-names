# Project Name : Gender Classifier for Indonesian Names
# Author : sinubi
# 

import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

def setup():
	nubi_stuff = pd.read_pickle(r'./nubi.stuff')
	return nubi_stuff
	
def predict_string(nubi_stuff,nama):
	vectorizer = nubi_stuff["vectorizer"]
	model = nubi_stuff["model"]
	jenis_kelamin_label = {1:"pria", 0:"wanita"}
	x_test = vectorizer.transform([nama])
	pred_test = model.predict(x_test)
	pred_test_class = jenis_kelamin_label[int(pred_test)]
	return pred_test_class
	
def predict_dfColumn(nubi_stuff,series_kolomNama):
	vectorizer = nubi_stuff["vectorizer"]
	model = nubi_stuff["model"]
	jenis_kelamin_label = {1:"pria", 0:"wanita"}
	pred_list = []
	
	for index, value in series_kolomNama.items():
		x_test = vectorizer.transform([value])
		pred_test = model.predict(x_test)
		pred_test_class = jenis_kelamin_label[int(pred_test)]
		pred_list.append(pred_test_class)
	return pred_list