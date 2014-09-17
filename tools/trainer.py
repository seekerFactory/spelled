import collections, regex


class Trainer:
	def train(self, features):
		"""
		returns language model trained with Probability(frequency here)
		features:
		"""
		model = collections.defaultdict(lambda: 1)
		for f in features:
			model[f] += 1
		return model



	def expectence(self, features):
		"""
		returns model to identify bad cases
		features:
		"""
		model = collections.defaultdict(lambda: 1)
		return model



## NOT Yet in use, only for testing
	def bigWikiTrainer(self, features, verbose=True):
		"""
		train Error list with data provided by wiki common errors list
		features:
		"""

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
			if wrong in self.NWORDS:
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

		return model


