import collections, regex
from tools.wordProcessor import *

## def train(features):
## train Probability Model
## collections of defaultdict with information how many times each word appears in doccument forming languageModel
def train(features):
	model = collections.defaultdict(lambda: 1)
	for f in features:
		model[f] += 1
	return model


## def bigWikiTrainer(features, NWORDS, verbose=True):
## train Error list from wiki common errors list

def bigWikiTrainer(features, NWORDS, verbose=True):
## NOT COMPLETE

	if verbose:
		print("Creating Wiki common errors list")
		print("WikiModel is of type [Error=>Correction] hence opp of NModel")
		print("Number of examples: %d" % (len(features)))

	model = collections.defaultdict(lambda: 1)
	
	for line in features:
		##  For the last blank in raw data, will remove from here and move into bookreading
		if len(line) == 0:
			features.remove(line)
			continue
		
		(wrong, targets) = set(regex.split("->", line))
		if wrong in NWORDS:
			if verbose: 
				print("%r->%r" % (targets, wrong))
				#print("%r:  correct(%r) => %r" % (line, wrong, targets))
				#print("Wrong Word: %r in NWORDS for case %r" % (wrong, line))
			model[targets] = wrong
		else:
			if verbose:
				print("Not in NWORDS %r" %(line))
			model[wrong] = targets
			#print("%r:  correct(%r) => %r" % (line, wrong, targets))
		#line = removeSChars(fo.readline())
		#else print("%r:  correct(%r) => %r" % (line, wrong, targets))
		#print(regex.split("->", line))

	if verbose: print("*****train2******fin*")
	return model


