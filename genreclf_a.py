import numpy as np

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
countForWordsRap = np.zeros(len(wordsArray)); #stores counts.
countForWordsRockPop = np.zeros(len(wordsArray));
countForWordsCountry = np.zeros(len(wordsArray));

probabilityForGenre = 1000/3000.0;
probabilitiesForWords = np.zeros(len(wordsArray));
probabilitiesForWordsRap = np.zeros(len(wordsArray));
probabilitiesForWordsRockPop = np.zeros(len(wordsArray));
probabilitiesForWordsCountry = np.zeros(len(wordsArray));

tracksArray = np.load('csc475_asn3_data/tracks.pck');

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

	
print 'Results For Rap';
for i in range(len(wordsArray)):	
	print("%6s:%6d "% (wordsArray[i],countForWordsRap[i]));
print;

print 'Results For Rock Pop';
for i in range(len(wordsArray)):	
	print("%6s:%6d "% (wordsArray[i],countForWordsRockPop[i]));
print;

print 'Results For Country';
for i in range(len(wordsArray)):	
	print("%6s:%6d "% (wordsArray[i],countForWordsCountry[i]));
print;

#compute the probabilites
		
#a. get overall probability P(word) = is N_inst_with_Word / 3000;

for i in range (len(wordsArray)):
	#probs for individual word in the whole dataset
	probabilitiesForWords[i] =  (countForWordsRap[i]+countForWordsRockPop[i]+countForWordsCountry[i])/3000.0;
	
	#conditional probs. --- Using general multiplication rule.
	#  Since P(A and B) = P(A) * P(B|A) 
    #  P(B|A) = P(A and B) / P(A)
    #  P(word|genre) = P(word and genre) / P(genre);

	#  P(word and genre) = #instances with the word that are that genre /  total number of instances.
	#  P(genre) = 1/3.
	
	probabilitiesForWordsRap[i] = (countForWordsRap[i]/3000.0)/probabilityForGenre;
	probabilitiesForWordsRockPop[i] = (countForWordsRockPop[i]/3000.0)/probabilityForGenre;
	probabilitiesForWordsCountry[i] = (countForWordsCountry[i]/3000.0)/probabilityForGenre;

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
	




