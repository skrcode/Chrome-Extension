import logging
def do(train_sentences):
	# Import the built-in logging module and configure it so that Word2Vec 
	# creates nice output messages
	
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',\
	    level=logging.INFO)

	# Set values for various parameters
	num_features = 300    # Word vector dimensionality                      
	min_word_count = 40   # Minimum word count                        
	num_workers = -1       # Number of threads to run in parallel
	context = 10          # Context window size                                                                                    
	downsampling = 1e-3   # Downsample setting for frequent words

	# Initialize and train the model (this will take some time)
	from gensim.models import word2vec
	print "Training model..."
	model = word2vec.Word2Vec(train_sentences, workers=num_workers, \
	            min_count = min_word_count, \
	            window = context, sample = downsampling)

	# If you don't plan to train the model any further, calling 
	# init_sims will make the model much more memory-efficient.
	model.init_sims(replace=True)

	# It can be helpful to create a meaningful model name and 
	# save the model for later use. You can load it later using Word2Vec.load()
	model_name = "Word2Vec_AnswerClass"
	model.save(model_name)
	print "Training complete..!!"
	return model