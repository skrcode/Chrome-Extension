from sklearn.cluster import KMeans
import time
import numpy as np
import get_sentences
import cPickle

def create_bag_of_centroids( wordlist, word_centroid_map ):
	#
	# The number of clusters is equal to the highest cluster index
	# in the word / centroid map
	num_centroids = max( word_centroid_map.values() ) + 1
	#
	# Pre-allocate the bag of centroids vector (for speed)
	bag_of_centroids = np.zeros( num_centroids, dtype="float32" )
	#
	# Loop over the words in the review. If the word is in the vocabulary,
	# find which cluster it belongs to, and increment that cluster count 
	# by one
	for word in wordlist:
	    if word in word_centroid_map:
	        index = word_centroid_map[word]
	        bag_of_centroids[index] += 1
	#
	# Return the "bag of centroids"
	return bag_of_centroids

def initialize_kmeans(model):
	start = time.time() # Start time

	# Set "k" (num_clusters) to be 1/5th of the vocabulary size, or an
	# average of 5 words per cluster
	word_vectors = model.syn0
	num_clusters = word_vectors.shape[0] / 5

	# Initalize a k-means object and use it to extract centroids
	kmeans_clustering = KMeans( n_clusters = num_clusters )
	idx = kmeans_clustering.fit_predict( word_vectors )

	# Get the end time and print how long the process took
	end = time.time()
	elapsed = end - start
	print "Time taken for K Means clustering: ", elapsed, "seconds."

	# Create a Word / Index dictionary, mapping each vocabulary word to
	# a cluster number                                                                                            
	word_centroid_map = dict(zip( model.index2word, idx ))
	with open('variables/word_centroid_map', 'wb') as f:
		cPickle.dump(word_centroid_map, f)
	with open('variables/num_clusters', 'wb') as f:
		cPickle.dump(num_clusters, f)
	return word_centroid_map,num_clusters

def printclusters(word_centroid_map,n):
	# For the first n clusters
	for cluster in xrange(0,n):
		#
		# Print the cluster number  
		print "\nCluster %d" % cluster
		#
		# Find all of the words for that cluster number, and print them out
		words = []
		for i in xrange(0,len(word_centroid_map.values())):
			if( word_centroid_map.values()[i] == cluster ):
				words.append(word_centroid_map.keys()[i])
		print words

def get_bag_of_centroids(word_centroid_map,num_clusters,X_train,X_test):

	clean_train_reviews = []
	for review in X_train["review"]:
		clean_train_reviews.append( get_sentences.review_to_wordlist( review, remove_stopwords=True ))
	clean_test_reviews = []
	for review in X_test["review"]:
		clean_test_reviews.append( get_sentences.review_to_wordlist( review, remove_stopwords=True ))


	# Pre-allocate an array for the training set bags of centroids (for speed)
	train_centroids = np.zeros( (X_train["review"].size, num_clusters), \
    	dtype="float32" )

	# Transform the training set reviews into bags of centroids
	counter = 0
	for review in clean_train_reviews:
		train_centroids[counter] = create_bag_of_centroids( review, \
			word_centroid_map )
		counter += 1

	# Repeat for test reviews 
	test_centroids = np.zeros(( X_test["review"].size, num_clusters), \
		dtype="float32" )

	counter = 0
	for review in clean_test_reviews:
		test_centroids[counter] = create_bag_of_centroids( review, \
			word_centroid_map )
		counter += 1

	return train_centroids,test_centroids

def get_bag_of_centroids_test(word_centroid_map,num_clusters,review):

	clean_test_reviews = []
	clean_test_reviews.append( get_sentences.review_to_wordlist( review, remove_stopwords=True ))

	# Repeat for test reviews 
	test_centroids = np.zeros((1, num_clusters), \
		dtype="float32" )

	counter = 0
	for review in clean_test_reviews:
		test_centroids[counter] = create_bag_of_centroids( review, \
			word_centroid_map )
		counter += 1

	return test_centroids

def do(model,X_train,X_test):
	word_centroid_map,num_clusters = initialize_kmeans(model)
	#printclusters(word_centroid_map,100)
	train_centroids,test_centroids = get_bag_of_centroids(word_centroid_map,num_clusters,X_train,X_test)
	return train_centroids,test_centroids