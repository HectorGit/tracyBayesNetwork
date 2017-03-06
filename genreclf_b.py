import numpy as np
import findProbabilities

class genreclf_b():

	def main():
	
		data = np.load('csc475_asn3_data/data.npz');
		dataArray = data['arr_0'];
		labels = np.load('csc475_asn3_data/labels.npz');
		labelsArray = labels['arr_0'];
		genres = dict([(12,'Rap'), (1,'Rock Pop'),(3,'Country')]);
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
		tracksArray = np.load('csc475_asn3_data/tracks.pck');
		findProbabilities.trainModel(dataArray, labelsArray, genres, wordsArray, probabilitiesForWords,probabilitiesForWordsRap,probabilitiesForWordsRockPop,probabilitiesForWordsCountry);
		print 'Probabilities per word';
		for i in range(len(wordsArray)):	
			print("%6s : %0.5f "% (wordsArray[i],probabilitiesForWords[i]));
		print;
		print 'Probabilities For Rap';
		for i in range(len(wordsArray)):	
			print("%6s : %0.5f "% (wordsArray[i],probabilitiesForWordsRap[i]));
		print;
		print 'Probabilities For Rock Pop';
		for i in range(len(wordsArray)):	
			print("%6s : %0.5f "% (wordsArray[i],probabilitiesForWordsRockPop[i]));
		print;
		print 'Probabilities For Country';
		for i in range(len(wordsArray)):	
			print("%6s : %0.5f "% (wordsArray[i],probabilitiesForWordsCountry[i]));
		print;
		classification = findProbabilities.testModel(dataArray, labelsArray, genres, wordsArray, probabilitiesForWords,probabilitiesForWordsRap,probabilitiesForWordsRockPop,probabilitiesForWordsCountry);	
		findProbabilities.accuracyAndConfusionMatrix(classification, labelsArray);
		return 0;

	if __name__ == "__main__": main()
                          