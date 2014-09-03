#! /usr/bin/env python3

import unicodedata as ud

from testCases import *
from tools.ngram import NGram as NG



################ Testing code from here on ################
## (correction) = (correct(wrong))
## When (correction) != (target) : P(expected) < P(correction)
## When (correction) != (target) : (bad increases)
## When (target) not in NWORDS :  unknown word

def enzymetest(tests, ng, bias=None, verbose=True):
	import time
	n, bad, unknown, start = 0, 0, 0, time.clock()
	if bias:
		for target in tests:
			ng.NWORDS[target] += bias
	for target,wrongs in tests.items():
		for wrong in wrongs.split():
			n += 1
##			w = correct(wrong)
			candidates = ng.correctSet(wrong)
			w=max(candidates, key=ng.NWORDS.get)
			diff= ng.NWORDS[w] - ng.NWORDS[target]
			if w!=target:
				bad += 1
				unknown += (target not in ng.NWORDS)
				if verbose:
					if ((diff > 0) and (diff < 10) and (ng.NWORDS[target]==1)):
						
						print('for set [[%s]],  Diff bw (correct(%s): %s(%d)) & (expected: %s(%d)) is %d'%(candidates, wrong, w, ng.NWORDS[w], target, ng.NWORDS[target], diff))
##					print('correct(%r) => %r (%d); expected %r (%d)' % (wrong, w, NWORDS[w], target, NWORDS[target]))
	
	return dict(bad=bad, n=n, bias=bias, pct=int(100. - 100.*bad/n), unknown=unknown, secs=int(time.clock()-start))



## Will be adding unown words into NWORDS for bad cases,
## else increase  P(target) with difference in mean of P(target) and P(cw),
## which increases next time chances if possible to reach through our correction algorithm.
def learned(tests, ng, bias=None, verbose=True):
	import time
	n, bad, unknown, start = 0, 0, 0, time.clock()
	print("********** Learned *************")
	if bias:
		for target in tests:
			ng.NWORDS[target] += bias
	for target,wrongs in tests.items():
		for wrong in wrongs.split():
			n += 1
			## This is for multiple runs, as we already know (expected of wrong) word.
			## Hence not again calling correct(wrong)
			if(wrong in ng.EXPECTENCE):
				w = ng.EXPECTENCE[wrong]
			else:
				w = ng.correct(wrong)
			if w!=target:
				bad += 1
				if (target not in ng.NWORDS):
					unknown +=1;
					## This is creating error model
					ng.EXPECTENCE[wrong] = target;

				else:
					ng.NWORDS[target] += int(abs(ng.NWORDS[target] - ng.NWORDS[w])/2)

				if verbose:
					print('correct(%r) => %r (%d); expected %r (%d)' % (wrong, w, ng.NWORDS[w], target, ng.NWORDS[target]))
	
	return dict(bad=bad, n=n, bias=bias, pct=int(100. - 100.*bad/n), unknown=unknown, secs=int(time.clock()-start))





if __name__ == '__main__':
#def main():

########## Change these as needed #############
	lang = "english"
	bias, verbose, timesrun = None, True, 1
###############################################

	dataset=[]
	ng = NG(lang)

	for i in range(timesrun):
		dataset.append(("Ran "+str(i+1), enzymetest(test2.test(), ng, bias, verbose)))
		if bias:
			bias = None

	for item in dataset: print(item)
#	print(EXPECTENCE)

#if __name__ == '__main__':
#`	main()
