#! /usr/bin/env python3

import unicodedata as ud

from testCases import *
#from tools.clstrainer import *
from tools.ngram import NGram as NG


################ Testing code from here on ################
## (correction) = (correct(wrong))
## When (correction) != (target) : P(expected) < P(correction)
## When (correction) != (target) : (bad increases)
## When (target) not in NWORDS :  unknown word

def spelltest(tests, ng, bias=None, verbose=True):
	import time

	n, bad, unknown, start = 0, 0, 0, time.clock()
	if bias:
		for target in tests:
			ng.NWORDS[target] += bias


	for target,wrongs in tests.items():
		for wrong in wrongs.split():
			n += 1
			w = ng.correct(wrong)
			if w!=target:
				bad += 1
				unknown += (target not in ng.NWORDS)
			if verbose:
				print('correct(%r) => %r (%d); expected %r (%d)' % (wrong, w, ng.NWORDS[w], target, ng.NWORDS[target]))
    
	return dict(bad=bad, n=n, bias=bias, pct=int(100. - 100.*bad/n), unknown=unknown, secs=int(time.clock()-start))


def main():

## basic cases for fast testing with small number of examples.
## Choose one param ("english" | "hindi") for setGlobalsWithLanguage(param)
## Choose one param ("english" | "hindi" | "special") for basic.test(param), "special" only for "english" with examples with quotes etc

########## Change these as needed #############	
	lang, case = 'english', 'english'
#	lang, case = 'hindi', 'hindi'
	bias, verbose, timesrun = None, True, 1
############################################### 

	dataset=[];
	ng = NG(lang)

	print("------ Will print all examples------")
	for i in range(timesrun):
		dataset.append(("Ran "+str(i+1), spelltest(basic.test(case), ng, bias, verbose)));
		## When running multiple times reset bias to None for next runs, else bias will again be introduced into NWORDS  
		if bias:
			bias = None

	for item in dataset: print(item)

if __name__ == '__main__':
## if parsing params from outside, change def main(params, ..); main(params, ..); 
#import sys;

	main()
