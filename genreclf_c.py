import numpy as np
import findProbabilities2

class genreclf_b():

	def main():
		k = 10;
		data = np.load('csc475_asn3_data/data.npz');
		dataArray = data['arr_0'];
		indexes = np.arange(3000); 
		np.random.shuffle(indexes);
		labels = np.load('csc475_asn3_data/labels.npz');
		labelsArray = labels['arr_0'];
		newData = [[]*30]*3000;
		newLabels = np.zeros(3000);
		for i in range (3000):
			newData[i] = dataArray[indexes[i]];
			newLabels[i] = labelsArray[indexes[i]];
		words = np.load('csc475_asn3_data/words.npz');
		dictionary = np.load('csc475_asn3_data/dictionary.pck');
		wordsArray = [];
		for i in words['arr_0']:
			wordsArray.append(dictionary[i]);
		print;
		probabilitiesForWords = np.zeros(len(wordsArray));
		probabilitiesForWordsRap = np.zeros(len(wordsArray));
		probabilitiesForWordsRockPop = np.zeros(len(wordsArray));
		probabilitiesForWordsCountry = np.zeros(len(wordsArray));
		main_matrix = [[0,0,0],[0,0,0],[0,0,0]]; 
		main_accuracy = 0; 
		accuracySum = 0;
		for i in range (k):
			testingData = newData[i*300:(i+1)*300];
			labelsData = newLabels[i*300:(i+1)*300]; 
			findProbabilities2.trainModel(k,i, newData, newLabels, wordsArray, probabilitiesForWords,probabilitiesForWordsRap,probabilitiesForWordsRockPop,probabilitiesForWordsCountry);
			#if(i == k-1):
			#	print '------------Final Probabilities:-----------';
			#	print 'Probabilities per word';
			#	for i in range(len(wordsArray)):	
			#		print("%6s : %0.5f "% (wordsArray[i],probabilitiesForWords[i]));
			#	print;
			#	print 'Probabilities For Rap';
			#	for i in range(len(wordsArray)):	
			#		print("%6s : %0.5f "% (wordsArray[i],probabilitiesForWordsRap[i]));
			#	print;
			#	print 'Probabilities For Rock Pop';
			#	for i in range(len(wordsArray)):	
			#		print("%6s : %0.5f "% (wordsArray[i],probabilitiesForWordsRockPop[i]));
			#	print;
			#	print 'Probabilities For Country';
			#	for i in range(len(wordsArray)):	
			#		print("%6s : %0.5f "% (wordsArray[i],probabilitiesForWordsCountry[i]));
			#	print;
			classification = findProbabilities2.testModel(testingData, wordsArray, probabilitiesForWords,probabilitiesForWordsRap,probabilitiesForWordsRockPop,probabilitiesForWordsCountry);	
			accuracy = findProbabilities2.calculateAccuracy(classification,labelsData);
			accuracySum = accuracySum+accuracy;
			iterationConfusionMatrix = findProbabilities2.calculateConfusionMatrix(classification,labelsData);
			main_matrix = np.add(main_matrix, iterationConfusionMatrix );
		main_accuracy = accuracySum/k;
		main_accuracy = main_accuracy*100.0;
		labels = ["Rap","Rock Pop","Country"];
		categories = ["a","b","c"];
		print( "%8s %8s %8s" % (categories[0], categories[1], categories[2]));
		for i in range(3):
			print("%8d %8d %8d" %(main_matrix[i][0], main_matrix[i][1], main_matrix[i][2])),
			print("| %s = %s" % (categories[i],labels[i]));
		print;
		print("Accuracy: %0.2f %% " % main_accuracy );
		return 0;
	if __name__ == "__main__": main()
                          



