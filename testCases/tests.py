#! /usr/bin/env python3

import regex
from . import *
from tools.wordProcessor import WordProcessor as WP
from tools.ngram import NGram as NG




def checkLetter(ng, verbose=False, verboseType='all'):
	datapkg='corpus'
	book="eng/myBigErrorsList.txt"

	data=WP.readBook(WP, datapkg, book)
	words = regex.split("(\n+)", data)
	cletter, n="", 0;
	for word in words:
		if "\n" in word:
			cletter += str('\n')
		else:
			for w in regex.split("\W+", word):
				if len(w):
					n +=1
					if verbose:
## works fine but case issue remains with this piece 
						print("correct(%r) => %r" % (w, ng.correct(w.lower())))
					cletter += str(ng.correct(w.lower()) + str(" "))

	print("######## Original Txt ########")
	print(data)
	print("######## Txt After Correction ########")
	print(cletter)
	print("################")



################ Testing code from here on ################
## (correction) = (correct(wrong))
## When (correction) != (target) : P(expected) < P(correction)
## When (correction) != (target) : (bad increases)
## When (target) not in NWORDS :  unknown word

def spelltest(tests, ng, bias=None, verbose=False, verboseType='bad'):
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
				if verbose and verboseType=='bad':
					print('correct(%r) => %r (%d); expected %r (%d)' % (wrong, w, ng.NWORDS[w], target, ng.NWORDS[target]))

			if verbose and verboseType=='all':
				print('correct(%r) => %r (%d); expected %r (%d)' % (wrong, w, ng.NWORDS[w], target, ng.NWORDS[target]))
    
	return dict(bad=bad, n=n, bias=bias, pct=int(100. - 100.*bad/n), unknown=unknown, secs=int(time.clock()-start))


def tested(testcase, bias=None, lang='english',case='english', verbose=False, timesrun=1):

	dataset=[];
	ng = NG(lang)

	## verboseType='bad' for printing bad cases only
	## verboseType='all' for printing all checks(like in basic), fine for small example set 
	verboseType='bad'
	if verbose:
		if testcase=='basic': verboseType='all'
		print("++++++++++++ Will print %s cases +++++++++++++" %(verboseType))
	for i in range(timesrun):
		if verbose: print("========= Run %d ========" %(i+1))
		if testcase == 'test1': dataset.append(("Run "+str(i+1), spelltest(test1.test(), ng, bias, verbose, verboseType='bad')));
		elif testcase == 'test2':dataset.append(("Run "+str(i+1), spelltest(test2.test(), ng, bias, verbose, verboseType='bad')));
		elif testcase == 'basic':dataset.append(("Run "+str(i+1), spelltest(basic.test(case), ng, bias, verbose, verboseType='all')));
		elif testcase == 'filetest': checkLetter(ng, verbose, verboseType='all');
##		reset bias to None after 1st run else will keep on increasing 
		if bias:
			bias = None
	if not testcase=='filetest':
		print("Runs ended\n \t==== Final Result ====")
		for item in dataset: print(item)

