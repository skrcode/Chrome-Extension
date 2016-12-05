import data_read 
import train_word2vec
import vector_avg
import get_sentences
import centroid_bow
import train
import write_result

# Read Train and Test Files
X_train,X_test = data_read.do("data/test_data.csv")
# Get Word2Vec format sentences from data
train_sentences,test_sentences = get_sentences.do(X_train['review'],X_test['review'])
# Train Word2Vec model
model = train_word2vec.do(train_sentences)
# Get centroids Bag of Words
train_centroids,test_centroids = centroid_bow.do(model,X_train,X_test)
# Train a RandomForest to get results on test data
result = train.do(X_train,train_centroids,test_centroids)
# Output to file
write_result.do(result,X_test)