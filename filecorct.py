#! /usr/bin/env python3

#from tools.wordProcessor import *
import regex
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
					cletter += str(ng.correct(w) + str(" "))
    
	print("######## Original Txt ########")
	print(data)
	print("######## Txt After Correction ########")
	print(cletter)
	print("################")

if __name__ == '__main__':
	main()
