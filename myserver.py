#!flask/bin/python
from flask import Flask, jsonify
from flask import request
app = Flask(__name__)
from flask import abort
import run_test
import data_read 
import train_word2vec
import vector_avg
import get_sentences
import centroid_bow
import train
import write_result
import cPickle
from sklearn.externals import joblib

# Retrieve computed model
from gensim.models import Word2Vec
model = Word2Vec.load("Word2Vec_AnswerClass")
# Get centroids Bag of Words
with open('variables/num_clusters', 'rb') as f:
	num_clusters = cPickle.load(f)
with open('variables/word_centroid_map', 'rb') as f:
	word_centroid_map = cPickle.load(f)
# Test the saved RandomForest to get results on test data                                                                                                                                                                                                       
forest = joblib.load('models/forest')

@app.route('/classify', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)
    task = {
        'response' : run_test.compute_genre_test(word_centroid_map,num_clusters,forest,request.json['body'])
    }
    return jsonify({'task': task}), 201

if __name__ == '__main__':

	app.run(debug=True)