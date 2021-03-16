# Installation and Execution
	
	This project was written in Python 2.7.12 using pandas, sklearn, requests, time, and setuptools 5.4.1.
	
	The following steps should be followed to properly install the project:
	1. Once the files are downloaded from GitHub, navigate to the first NLP folder (root NLP) and ensure that the dependencies are all present in the root NLP folder.
	2. In the console, run the command: "python setup.py develop", which will build the project and allow for the entry points to be used.
	3. To test the individual challenges, simply use the challenge name as a command (challenge-1, challenge-2, or challenge-5) to execute the desired challenge.
	
	Note: Each challenge creates an external file, these files will appear in the root NLP folder.
	
	Challenge-1: produces newFile.csv
	Challenge-2: produces metrics.txt
	Challenge-5: produces web-download.html

## Dependencies

	Challenge-1:
	
	This challenge requires this [dataset] (https://catalog.data.gov/dataset/2006-2011-nys-math-test-results-by-grade-citywide-by-race-ethnicity) in csv format.
	Dataset courtesy of: [catalog.data.gov] (https://catalog.data.gov/dataset)
	Additionally pandas is a required import for this challenge.
	
	Challenge-2:
	
	This challenge requires the iris dataset which can be found [here] (https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data).
	sklearn and pandas are both required imports for this challenge.

	Challenge-5:
	
	This challenge does not require any additional files. However, it must have a stable internet connection in order to properly function.
	requests and time are required imports for this challenge.
	All imports are handled upon execution of the command: "python setup.py develop".


#### Author: Michael Blake Kelley
