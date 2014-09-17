#! /usr/bin/env python3

#from tools.wordProcessor import *
import regex, argparse
from tools.wordProcessor import WordProcessor as WP
from tools.ngram import NGram as NG


def main():
	lang="english"
	datapkg = "corpus"
	book = "eng/myBigErrorsList.txt"
	
	data = WP.readBook(WP, datapkg, book)
	#words = regex.split("(\n+)", data.lower())
	words = regex.split("(\n+)", data)
	ng = NG(lang)
	cletter, n ="", 0;
	for word in words:
		if "\n" in word:
			cletter += str('\n')
		else:
			for w in regex.split("\W+", word):
				if len(w):
					n +=1
					print("correct(%r) => %r" % (w, ng.correct(w.lower())))
					cletter += str(ng.correct(w.lower()) + str(" "))
    
	print("######## Original Txt ########")
	print(data)
	print("######## Txt After Correction ########")
	print(cletter)
	print("################")

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Check my book', add_help=True)
	parser.add_argument('-v', '--verbose',dest='verbose', action='store_true', help='verbose mode processing shown')
	parser.add_argument('-t', '--test',dest='testcase', action='store', choices={'test1', 'test2', 'basic', 'filecorct'}, default='test1',help='testcase name')
	args=parser.parse_args()

	if args.verbose:
		print(args.verbose)
	else:	print(args.testcase)

	main()
