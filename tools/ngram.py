import collections, regex
from tools.wordProcessor import *
from tools.trainer import *

## def known(words):
## returns list of known words(appeared in languagemodel) from [words] passed
def known(words): return set(w for w in words if w in NWORDS)


## def correct(word):
## Reasoning from norvig:
## All known words of edit_distance 1 are infinitely more probable than known words of edit_distance 2, and infinitely less probable than a known word of edit_distance 0
##
## candidates = set with shortest edit_distance to original word as long as set has known words
## After identifying candidate set it returns word with highest P(c) value estimated by NWORDS model
def correct(word):
	candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
	return max(candidates, key=NWORDS.get)

## def split_words(word):
## returns list of set(a, b) formed by breaking the word into two (a, b) eachtime
## word = a + b
## when len(word) is n there are n+1 elements in this list
def split_words(word):
	split_set = [(word[:i], word[i:]) for i in range(len(word)+1)]
	return split_set


## def edits1(word):
## returns a list of all edits which are at edit_distance 1
## all_edits = deletion_edits + transpostion_edits + alteration_edits + insertion_edits
## If (m: literarls in language, n: chars in word), 
## (n): deletions, (n-1): transposes, (mn): alterations, m(n+1): insertions
## Total_edits = (2n(m+1) + (m-1)) , at edit_distance 1
## spell correction literature claims 80% to 95% of spelling errors are at edit_distance 1 from target
def edits1(word):
	splits = split_words(word)
	deletes = [a + b[1:] for a, b in splits]
	transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
	alterations = [a + c + b[1:] for a, b in splits for c in alphabet if b]
	inserts =  [a + c + b     for a, b in splits for c in alphabet]
    
	return set(deletes + transposes + alterations + inserts)


## def known_edits2(word):
## returns the list of edits at edit_distance 2 and are known words
## known words helps reduce size of list
def known_edits2(word):
	return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)



#book = 'premchand.txt';
book = 'big.txt';
inPath = './corpus/eng';

NWORDS = train(wordsInText(readBook(book, inPath, True)));
#WIKIERRORS = bigWikiTrainer(wordsInText(readBook('bigWikiErrors.txt', inPath), "\n+"), NWORDS)
alphabet = charecterSet('english')
#alphabet = charecterSet('devanagari')
