Deprecated. New commit will be made soon to account for recent changes to www.quora.com<br/>
Chrome Extension for Quora<br/>
- Classifies Quora answers into genres such as information,stories and world affairs for improved reading experience<br/>
<br/>
To run<br/>
1. Load the src directory to Chrome Extensions in the Extensions menu in Google Chrome.<br/>
2. Run "python myserver.py". Install any dependencies, if required.<br/>
3. Go to "www.quora.com" and click on the Extension icon.<br/>
4. Click on "Load Unsafe Scripts" from the URL bar<br/>
5. Enjoy !<br/>


Notes:<br/>
The test data included contains data from the facebook page "Best-Of-Quora"<br/>

Gets labelled training data from python nltk's "Brown dataset". <br/>
Uses Google's Word2Vec to perform meaning analysis and get data points for each word. <br/>
Uses K means clustering to create an unsupervised model of for the list of words.<br/>
Associates each word to a cluster(centroid) and creates a bag of cluster model.<br/>
Using this bag of cluster vector for each paragraph, a RandomForest model with suitable parameter tuning is trained.<br/>
The test data is run on this model.<br/>

The Chrome Extension fetches data from the Quora home page and hits the python service and retrieves the output<br/>
