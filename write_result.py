import pandas as pd
def do(result,test):
	# Write the test results 
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
	output = pd.DataFrame(data={"id":test["id"], "genre":result})
	output.to_csv( "result.csv", index=False, quoting=3 )