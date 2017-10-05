import numpy as np

def trainModel(k,index, newData, newLabels , wordsArray, probabilitiesForWords,probabilitiesForWordsRap,probabilitiesForWordsRockPop,probabilitiesForWordsCountry):
	probabilityForGenre = 1000.0/3000.0;
	countForWordsRap = np.zeros(len(wordsArray)); 
	countForWordsRockPop = np.zeros(len(wordsArray));
	countForWordsCountry = np.zeros(len(wordsArray));
	number = 0;
	for i in range(k):
		if i != index:
			currentSubset = newData[i*300:(i+1)*300];
			countWords(number, currentSubset,newData,newLabels, wordsArray, countForWordsRap,countForWordsRockPop,countForWordsCountry);						
	for i in range (len(wordsArray)):
		probabilitiesForWords[i] =  (countForWordsRap[i]+countForWordsRockPop[i]+countForWordsCountry[i])/2700.0;
		probabilitiesForWordsRap[i] = (countForWordsRap[i]/2700.0)/probabilityForGenre;
		probabilitiesForWordsRockPop[i] = (countForWordsRockPop[i]/2700.0)/probabilityForGenre;
		probabilitiesForWordsCountry[i] = (countForWordsCountry[i]/2700.0)/probabilityForGenre;
		
def countWords(number, currentSubset, newData, newLabels, wordsArray, countForWordsRap, countForWordsRockPop, countForWordsCountry):
	for j in range(len(currentSubset)):
		genre = newLabels[j] ;
		for m in range(len(wordsArray)):
			if newData[j][m] > 0:
				if genre == 12:
					countForWordsRap[m] += 1;
				elif genre == 1:
					countForWordsRockPop[m] += 1;
				else:
					countForWordsCountry[m] +=1;

def testModel(testingData, wordsArray, probabilitiesForWords,probabilitiesForWordsRap,probabilitiesForWordsRockPop,probabilitiesForWordsCountry):
	probabilityForGenre = 1000/3000.0;
	classification = np.zeros(len(testingData));
	for i in range (len(testingData)):
		probabilityRap = probabilityForGenre;
		probabilityRockPop = probabilityForGenre;
		probabilityCountry = probabilityForGenre;
		for j in range (len(wordsArray)):
			if testingData[i][j]<=0:
				probabilityRap *= (1-probabilitiesForWordsRap[j]);
				probabilityRockPop *= (1-probabilitiesForWordsRockPop[j]);
				probabilityCountry *= (1-probabilitiesForWordsCountry[j]);
			if testingData[i][j]>0:
				probabilityRap *= probabilitiesForWordsRap[j];
				probabilityRockPop *= probabilitiesForWordsRockPop[j];
				probabilityCountry *= probabilitiesForWordsCountry[j]
		MAX_A_POST = np.argmax([probabilityRap, probabilityRockPop, probabilityCountry]);
		if(MAX_A_POST == 0):classification[i] = 12;
		elif(MAX_A_POST == 1):classification[i] = 1;
		elif(MAX_A_POST == 2):classification[i] = 3;				
	return classification;
	
def calculateAccuracy(classification,labelsArray):
	correctCounter = 0;
	for i in range (len(labelsArray)):
		if(classification[i] == labelsArray[i]):
			correctCounter += 1;
	totalInst = 300.0;
	accuracy = correctCounter/totalInst;
	return accuracy;
	
def calculateConfusionMatrix(classification,labelsArray):
	matrix = [[0,0,0],[0,0,0],[0,0,0]];
	for i in range (len(labelsArray)):
		if(classification[i] == labelsArray[i]):
			if labelsArray[i] == 12 and classification[i] == 12: matrix[0][0] += 1;
			elif labelsArray[i] == 1 and classification[i] == 1: matrix[1][1] += 1;
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
	return matrix;
	
	


