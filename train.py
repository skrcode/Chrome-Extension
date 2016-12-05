from sklearn.ensemble import RandomForestClassifier
import cPickle

def do(X_train,train_centroids,test_centroids):
	# Fit a random forest and extract predictions 
	forest = RandomForestClassifier(n_estimators = 700,min_samples_leaf=3,n_jobs=-1)

	# Fitting the forest may take a few minutes
	print "Fitting a random forest to labeled training data..."
	forest = forest.fit(train_centroids,X_train["genre"])

	from sklearn.externals import joblib
	joblib.dump(forest, 'models/forest') 


	result = forest.predict(test_centroids)
	return result
