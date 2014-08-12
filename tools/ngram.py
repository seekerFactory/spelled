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
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word];
    
    #if (len(word) > 0): print("k_word(%r) => k_edits1(%r) => k_edits2(%r) => for word %r" % (known([word]), known(edits1(word)), known_edits2(word), word));
    #if candidates == [word]: print("known_edits1(%r) for word %r" %((edits1(word)), word));

    
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
	alterations = [a + c + b[1:] for a, b in splits for c in _alphabet if b]
	inserts =  [a + c + b     for a, b in splits for c in _alphabet]
    
	return set(deletes + transposes + alterations + inserts)


## def known_edits2(word):
## returns the list of edits at edit_distance 2 and are known words
## known words helps reduce size of list
def known_edits2(word):
	return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)


## Very high dependency on _lang variable for selecting selecting other properties , set before calling train() with option(hindi | english)
_lang = "english";
_book=""; _inPath=""; _alphabet = "";
if _lang == 'english':
    _book = 'big.txt';
    _inPath = './corpus/eng';
    _alphabet = charecterSet('english')
elif _lang == 'hindi':
    _book = 'premchand.txt';
    _inPath = './corpus/brahmi';
    _alphabet = charecterSet('hindi')


NWORDS = train(wordsInText(readBook(_book, _inPath, True)));
#WIKIERRORS = bigWikiTrainer(wordsInText(readBook('bigWikiErrors.txt', inPath), "\n+"), NWORDS)
## will add word for bad cases in learned  as EXPECTENCE[word] = target
EXPECTENCE = train([]);

