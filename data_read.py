import pandas as pd
from nltk.corpus import brown
import data_clean

def do(file):
	# Read data from train
	X_train = pd.DataFrame(columns=('review','genre'))
	for genre in brown.categories():
		article = brown.paras(categories=genre)
		for review in article:
			X_train = X_train.append({'review':review, 'genre':genre}, ignore_index=True)
	# Read data from test
	X_test = pd.read_csv( file, header=0,delimiter="," )
	X_train = data_clean.convert_to_para(X_train)
	return X_train,X_test