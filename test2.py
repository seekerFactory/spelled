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
                unknown += (target not in NWORDS);
                if verbose:
                    print('correct(%r) => %r (%d); expected %r (%d)' % (wrong, w, NWORDS[w], target, NWORDS[target]))
    
    return dict(bad=bad, n=n, bias=bias, pct=int(100. - 100.*bad/n), unknown=unknown, secs=int(time.clock()-start))

if __name__ == '__main__':
######### Change these as needed #############
	lang = "english"
	bias, verbose, timesrun = None, True, 2
##############################################
	
	dataset=[];
	_lang, NWORDS = setGlobalsWithLanguage(lang);

	for i in range(timesrun):
		dataset.append(("Ran "+str(i+1), spelltest(test2.test(), bias, verbose)));
	
	for item in dataset: print(item)
