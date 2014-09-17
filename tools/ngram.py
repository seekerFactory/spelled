import collections
import time
from functools import wraps 

from . import WordProcessor as WP
from . import Trainer


## wrapper for checking time taken by each method
def timethis(debug=False):
	"""
	Decorator to check execution time and logging
	"""
	def decorate(func):
		if debug:
			print("testing decorator")

		@wraps(func)
		def wrapper(*args, **kwargs):
			start=time.time()
			result=func(*args, **kwargs)
			end=time.time()
			if debug:
				print("LoggingTime for method %s: %f"%(func.__name__, end-start))

			return result
		return wrapper
	return decorate

class NGram(WP, Trainer):

	def __init__(self, lang, expectence=False):
		"""
		lang:	language('english' || 'hindi') choosen to create language model
		expectence:	Used when learning from expected words
		"""

## Need to remove hard coded data from here and get into config file
		self.datapkg = 'corpus'
		self.lang = lang;

		if lang == "english":
			self.book = 'eng/big.txt'
		elif lang == 'hindi':
			self.book = 'brahmi/premchand.txt'
	

		self.alphabet = WP.charecterSet(self, self.lang);
		data = WP.readBook(self, self.datapkg, self.book)

		wordsinbook = WP.wordsInText(self, data, self.alphabet);

		self.NWORDS = Trainer.train(self, wordsinbook);

		#self.SPLITTED = Trainer.expectence()

	


	def known(self, words):
		"""
		Returns set of known words(appeared in languagemodel) from [words] passed
		words:	list of words
		"""
		return set(w for w in words if w in self.NWORDS)

	def correct(self, word):
		"""
		Returns word with highest P(c) | frequency value estimated by language model for given word edits.
		word:	word passed for correction

		candidates = set(known words(shortest edit_distance to original word))
		Known words @edit_distance1 are infinitely more probable than known words @edit_distance2 and infinitely less probable than known word @edit_distance0
		"""
# Need to remove multiple calls to edits1 from known_edits2 as it only needs the results of edits1
		edits1set=self.edits1(word)
		#candidates = self.known([word]) or self.known(edits1set) or self.known_edits2(edits1set) or [word];
		try:
			candidates = self.known([word]) or self.known(edits1set) or self.known_edits2(edits1set) or [word];
		except Exception as e:
			print(" :( **** Error raised *** ); ")
			print("Reason: ", e)

    
		return max( candidates, key=self.NWORDS.get); 


	def correctSet(self, word):
		"""
		Returns set(candidates) for given word.
		word:	word passed for correction

		candidates = set(known words(shortest edit_distance to original word))
		Known words @edit_distance1 are infinitely more probable than known words @edit_distance2 and infinitely less probable than known word @edit_distance0
		"""
		edits1set=self.edits1(word)
		candidates = self.known([word]) or self.known(edits1set) or self.known_edits2(edits1set) or [word];
		#candidates = self.known([word]) or self.known(edits1set) or self.known_edits2(word, edits1set) or [word];

		return candidates

	def split_words(self, word):
		"""
		Returns list of set(a, b) formed by breaking the word into (a, b) for each char
		word:	word passed for correction

		If len(word) is n there are n+1 elements in this list
		"""
		split_set = [(word[:i], word[i:]) for i in range(len(word)+1)]
		return split_set

#	@timethis(False)
	def edits1(self, word):
		"""
		Returns set of edits(deletes, transposes, alterations, inserts) at edit_distance 1.
		word:	word passed for correction 
		For (m: literarls in language, n: chars in word), there are 
			(n): deletions, (n-1): transposes, (mn): alterations, m(n+1): insertions
			Total_edits = (2n(m+1) + (m-1)) , at edit_distance 1
		"""
		splits = self.split_words(word)
		deletes = [a + b[1:] for a, b in splits]
		transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
		alterations = [a + c + b[1:] for a, b in splits for c in self.alphabet if b]
		inserts =  [a + c + b     for a, b in splits for c in self.alphabet]
		return set(deletes + transposes + alterations + inserts)




	def known_edits2(self, edits1set):
		"""
		Returns set of edits at edit_distance 2 and are known words, known words reduces size of set.  
		edits1set:	set of word @edit_distance 1
		"""
		return set(e2 for e1 in edits1set for e2 in self.edits1(e1) if e2 in self.NWORDS)

