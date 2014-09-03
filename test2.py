#! /usr/bin/env python3

import unicodedata as ud

from testCases import *
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
				unknown += (target not in ng.NWORDS);
				if verbose:
					print('correct(%r) => %r (%d); expected %r (%d)' % (wrong, w, ng.NWORDS[w], target, ng.NWORDS[target]))

	return dict(bad=bad, n=n, bias=bias, pct=int(100. - 100.*bad/n), unknown=unknown, secs=int(time.clock()-start))

#if __name__ == '__main__':
def main():
    
######### Change these as needed #############
	lang = "english"
	bias, verbose, timesrun = 10, True, 2
##############################################
	dataset=[];
	ng = NG(lang)
	if verbose: print("++++++++++++ Will print bad cases +++++++++++++")
	
	for i in range(timesrun):
		if verbose: print("========= Run %d ========" %(i+1))
		dataset.append(("Ran "+str(i+1), spelltest(test2.test(), ng, bias, verbose)));
		if bias:
			bias = None
	
	print("Runs ended\n \t==== Final Result ====")
	for item in dataset: print(item)

if __name__ == '__main__':
	main()
