#! /usr/bin/env python3

from tools.wordProcessor import * 
from tools.trainer import *
from tools.ngram import *

def filecorrect():
    ''' to correct the file passed '''
    book='myBigErrorsList.txt';
    inPath='./corpus/eng';
    str="/"
    f = open(str.join((inPath, book)), encoding='utf-8')
    lines = f.read()
    return lines

    #return wordsInText(readBook(book, inPath, True))

if __name__ == '__main__':
    lang="english"
    lines = filecorrect()
    words = regex.split("(\n+)", lines.lower())
    _lang, NWORDS = setGlobalsWithLanguage(lang)
    cletter, n ="", 0;
    print(words)
    for word in words:
        if "\n" in word:
            cletter += str('\n')
        else:
            for w in regex.split("\W+", word):
                if len(w):
                    n +=1
                    print("correct(%r) => %r" % (w, correct(w)))
                    cletter += str(correct(w) + str(" "))
    
    print("######## Original ########")
    print(lines)
    print("######## After Correction ########")
    print(cletter)
    print("################")
