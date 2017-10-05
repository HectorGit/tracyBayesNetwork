import numpy as np

def generate5Songs(probabilitiesArray, wordsArray):
	print '-----------------------------------------------------'

	numSongs = 5;
	limit = 30;
	wordsInSong = [];

	for n in range(numSongs):
		for m in range(limit):	
			randomProbability = np.random.random();
			randomIndex = np.random.randint(0,limit);
			if(randomProbability > probabilitiesArray[randomIndex]):
				wordsInSong = np.append(wordsInSong,wordsArray[randomIndex]);
		print wordsInSong;
		wordsInSong = [];			

	print '-----------------------------------------------------'
