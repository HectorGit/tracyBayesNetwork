import findProbabilities
import auxForGenerateSongs
import numpy as np

class generateSongs():
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
		findProbabilities.trainModel(dataArray, labelsArray, genres, wordsArray, probabilitiesForWords,probabilitiesForWordsRap,probabilitiesForWordsRockPop,probabilitiesForWordsCountry);
				
		#generate 5 rap songs
		print 'Generating 5 Rap Songs'
		auxForGenerateSongs.generate5Songs(probabilitiesForWordsRap, wordsArray);
		
		#generate 5 rock pop songs
		print 'Generating 5 Rock Pop Songs'
		auxForGenerateSongs.generate5Songs(probabilitiesForWordsRockPop, wordsArray);

		#generate 5 country songs
		print 'Generating 5 Country Songs'
		auxForGenerateSongs.generate5Songs(probabilitiesForWordsCountry, wordsArray);
				
		return 0;
	if __name__ == "__main__": main()
