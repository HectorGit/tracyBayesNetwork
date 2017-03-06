import numpy as np

def trainModel(dataArray, labelsArray, genres, wordsArray, probabilitiesForWords,probabilitiesForWordsRap,probabilitiesForWordsRockPop,probabilitiesForWordsCountry):
	probabilityForGenre = 1000/3000.0;
	countForWordsRap = np.zeros(len(wordsArray)); 
	countForWordsRockPop = np.zeros(len(wordsArray));
	countForWordsCountry = np.zeros(len(wordsArray));
	previousGenre = '';
	for i in range(len(dataArray)):
		currentGenre = labelsArray[i];
		if(currentGenre != previousGenre):
			print("Currently analysing: %s" % genres[currentGenre]);
			print;
		for j in range (len(wordsArray)):
			if dataArray[i][j] > 0:
				if currentGenre == 12:
					countForWordsRap[j] += 1;
				elif currentGenre == 1:
					countForWordsRockPop[j] += 1;
				else:
					countForWordsCountry[j] +=1;
		previousGenre = currentGenre;
	for i in range (len(wordsArray)):
		probabilitiesForWords[i] =  (countForWordsRap[i]+countForWordsRockPop[i]+countForWordsCountry[i])/3000.0;
		probabilitiesForWordsRap[i] = (countForWordsRap[i]/3000.0)/probabilityForGenre;
		probabilitiesForWordsRockPop[i] = (countForWordsRockPop[i]/3000.0)/probabilityForGenre;
		probabilitiesForWordsCountry[i] = (countForWordsCountry[i]/3000.0)/probabilityForGenre;


def testModel(dataArray, labelsArray, genres, wordsArray, probabilitiesForWords,probabilitiesForWordsRap,probabilitiesForWordsRockPop,probabilitiesForWordsCountry):
	probabilityForGenre = 1000/3000.0;
	classification = np.zeros(len(dataArray));
	for i in range (len(dataArray)):
		probabilityRap = probabilityForGenre;
		probabilityRockPop = probabilityForGenre;
		probabilityCountry = probabilityForGenre;
		for j in range (len(wordsArray)):
			if dataArray[i][j]<=0:
				probabilityRap *= (1-probabilitiesForWordsRap[j]);
				probabilityRockPop *= (1-probabilitiesForWordsRockPop[j]);
				probabilityCountry *= (1-probabilitiesForWordsCountry[j]);
			if dataArray[i][j]>0:
				probabilityRap *= probabilitiesForWordsRap[j];
				probabilityRockPop *= probabilitiesForWordsRockPop[j];
				probabilityCountry *= probabilitiesForWordsCountry[j]
		MAX_A_POST = np.argmax([probabilityRap, probabilityRockPop, probabilityCountry]);
		if(MAX_A_POST == 0):classification[i] = 12;
		elif(MAX_A_POST == 1):classification[i] = 1;
		elif(MAX_A_POST == 2):classification[i] = 3;				
	return classification;
	
def accuracyAndConfusionMatrix(classification,labelsArray):
	correctCounter = 0;
	matrix = [[0,0,0],[0,0,0],[0,0,0]];
	for i in range (len(labelsArray)):
		if(classification[i] == labelsArray[i]):
			correctCounter += 1;
			#rap
			if labelsArray[i] == 12 and classification[i] == 12: matrix[0][0] += 1;
			#rock pop
			elif labelsArray[i] == 1 and classification[i] == 1: matrix[1][1] += 1;
			#country
			elif labelsArray[i] == 3 and classification[i] == 3: matrix[2][2] += 1;
		else:
			#rap classified as rock pop
			if labelsArray[i] == 12 and classification[i] == 1: matrix[0][1] += 1;
			#rap classified as country
			elif labelsArray[i] == 12 and classification[i] == 3: matrix[0][2] += 1;
			#rock pop classified as rap
			elif labelsArray[i] == 1 and classification[i] == 12: matrix[1][0] += 1;
			#rock pop classified as country
			elif labelsArray[i] == 1 and classification[i] == 3: matrix[1][2] += 1;
			#country classified as rap
			elif labelsArray[i] == 3 and classification[i] == 12: matrix[2][0] += 1;
			#country classf as rock pop
			elif labelsArray[i] == 3 and classification[i] == 1: matrix[2][1] += 1;
	totalInst = 3000.0;
	accuracy = correctCounter/totalInst;
	accuracyPercentage = accuracy*100.0;     
	labels = ["Rap","Rock Pop","Country"];
	categories = ["a","b","c"];
	print( "%8s %8s %8s" % (categories[0], categories[1], categories[2]));
	for i in range(3):
		print("%8d %8d %8d" %(matrix[i][0], matrix[i][1], matrix[i][2])),
		print("| %s = %s" % (categories[i],labels[i]));
	print;
	print("Accuracy: %0.2f %% " % accuracyPercentage );

	
	


