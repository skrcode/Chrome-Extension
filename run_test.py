import data_read 
import train_word2vec
import vector_avg
import get_sentences
import centroid_bow
import train
import write_result
import cPickle
from sklearn.externals import joblib
def compute_genre_test(word_centroid_map,num_clusters,forest,review):

	test_centroids = centroid_bow.get_bag_of_centroids_test(word_centroid_map,num_clusters,review)
	result = forest.predict(test_centroids)
	i = 0
	for row in result:
		if row == "news":
			result[i] = "information"
		if row == "belles_lettres":
			result[i] = "stories"
		if row == "romance":
			result[i] = "romance & emotions"
		if row == "government":
			result[i] = "world affairs"
		if row == "learned":
			result[i] = "knowledge"
		i = i + 1
	return result[0]