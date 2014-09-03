import collections, regex

from . import WordProcessor as WP
from . import Trainer
#from tools.clswordProcessor import WordProcessor
#from tools.clstrainer import Trainer



class NGram(WP, Trainer):
## Very high dependency on _lang variable for selecting selecting other properties , set before calling train() with option(hindi | english)
#	_lang = "";
#	_book=""; _inPath=""; _alphabet = "";
#	NWORDS=train([]);
#	EXPECTENCE=train([]);

	def __init__(self, lang, expectence=False):
	
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
		#self.NWORDS = Trainer.train(self, WP.wordsInText(self, WP.newreadBook(self, 'eng/big.txt'), self._alphabet));

		#if (expectence == False):
			#return (self._lang, self.NWORDS)
		#elif (expectence == True):
			#return (self._lang, self.NWORDS, self.EXPECTENCE)

	## Still havn't started using WIKIERRORS
	#WIKIERRORS = bigWikiTrainer(wordsInText(readBook('bigWikiErrors.txt', inPath), "\n+"), NWORDS)


## def known(words):
## returns list of known words(appeared in languagemodel) from [words] passed
	def known(self, words):
		return set(w for w in words if w in self.NWORDS)


## def correct(word):
## Reasoning from norvig:
## All known words of edit_distance 1 are infinitely more probable than known words of edit_distance 2, and infinitely less probable than a known word of edit_distance 0
##
## candidates = set with shortest edit_distance to original word as long as set has known words
## After identifying candidate set it returns word with highest P(c) value estimated by NWORDS model
	def correct(self, word):
		candidates = self.known([word]) or self.known(self.edits1(word)) or self.known_edits2(word) or [word];
    
		return max(candidates, key=self.NWORDS.get)


## Same as correct(word), identifying max(candidates) set
	def correctSet(self, word):
		candidates = self.known([word]) or self.known(self.edits1(word)) or self.known_edits2(word) or [word];

##	print('candidateSet [[%s]]' %(candidates))
##	for c in candidates:
##		keyval=NWORDS[c]
##		maxInSet = max(c, key=NWORDS.get)
##		print('For cadidate [[ %s:(%d) ]] ' %(c, keyval))

##	return max(candidates, key=NWORDS.get)

		return candidates

## def split_words(word):
## returns list of set(a, b) formed by breaking the word into two (a, b) eachtime
## word = a + b
## when len(word) is n there are n+1 elements in this list
	def split_words(self, word):
		split_set = [(word[:i], word[i:]) for i in range(len(word)+1)]
		return split_set


## def edits1(word):
## returns a list of all edits which are at edit_distance 1
## all_edits = deletion_edits + transpostion_edits + alteration_edits + insertion_edits
## If (m: literarls in language, n: chars in word), 
## (n): deletions, (n-1): transposes, (mn): alterations, m(n+1): insertions
## Total_edits = (2n(m+1) + (m-1)) , at edit_distance 1
## spell correction literature claims 80% to 95% of spelling errors are at edit_distance 1 from target
	def edits1(self, word):
		splits = self.split_words(word)
		deletes = [a + b[1:] for a, b in splits]
		transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
		alterations = [a + c + b[1:] for a, b in splits for c in self.alphabet if b]
		inserts =  [a + c + b     for a, b in splits for c in self.alphabet]
		return set(deletes + transposes + alterations + inserts)


## def known_edits2(word):
## returns the list of edits at edit_distance 2 and are known words
## known words helps reduce size of list
	def known_edits2(self, word):
		return set(e2 for e1 in self.edits1(word) for e2 in self.edits1(e1) if e2 in self.NWORDS)


