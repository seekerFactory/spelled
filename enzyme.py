#! /usr/bin/env python3

import unicodedata as ud

from testCases import *
from tools.trainer import *
from tools.ngram import *



################ Testing code from here on ################
## (correction) = (correct(wrong))
## When (correction) != (target) : P(expected) < P(correction)
## When (correction) != (target) : (bad increases)
## When (target) not in NWORDS :  unknown word

def spelltest(tests, bias=None, verbose=True):
	import time
	n, bad, unknown, start = 0, 0, 0, time.clock()
	if bias:
		for target in tests:
			NWORDS[target] += bias
	for target,wrongs in tests.items():
		for wrong in wrongs.split():
			n += 1
			w = correct(wrong)
			if w!=target:
				bad += 1
				unknown += (target not in NWORDS)
				if verbose:
					print('correct(%r) => %r (%d); expected %r (%d)' % (wrong, w, NWORDS[w], target, NWORDS[target]))
	
	return dict(bad=bad, n=n, bias=bias, pct=int(100. - 100.*bad/n), unknown=unknown, secs=int(time.clock()-start))



## Will be adding unown words into NWORDS
## adding probability diff mean of bad known cases
def learned(tests, bias=None, verbose=True):
	import time
	n, bad, unknown, start = 0, 0, 0, time.clock()
	print("********** Learned *************")
	if bias:
		for target in tests:
			NWORDS[target] += bias
	for target,wrongs in tests.items():
		for wrong in wrongs.split():
			n += 1
			w = correct(wrong)
			if w!=target:
				bad += 1
				if (target not in NWORDS):
					unknown +=1
					NWORDS[target] = 1
#				elif NWORDS[target] > NWORDS[w]:

				if verbose:
					print('correct(%r) => %r (%d); expected %r (%d)' % (wrong, w, NWORDS[w], target, NWORDS[target]))
	
	return dict(bad=bad, n=n, bias=bias, pct=int(100. - 100.*bad/n), unknown=unknown, secs=int(time.clock()-start))





if __name__ == '__main__':
	words_hin = ["हिन्दी", "घार", "घर", "घरम"]
	words_eng = ["imposible", "wort", "rmov", "pag"]

#	for word in words_eng:
#		for c in word:
#			print(c, ud.category(c), ud.name(c))

#		print('CorrectOf(%r) => %r\n' % (word, correct(word)))
    
    # print(learnpy(test1.test()))
	dataset=[]
	for i in range(3):
		dataset.append((i, spelltest(test1.test())))

	for item in dataset: print(item)