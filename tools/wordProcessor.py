import regex


def removeNLine(line):
	return regex.sub(r"(\n)", r"", line)

def removeSChars(line):
## will seperate sChars and pass name, as param,  to be removed 
	sChars = [r"(\n)", r"(\,)", r"(\!)", r"(\?)", r"(\:)", r"(\;)", r"(\()", r"(\))", chr(0x0964), chr(0x0965), chr(0x097D)]
	for char in sChars:
		line = regex.sub(char, r"", line)
	return line
							
def wordsInText(text, seperator="\s+"):
	## Word seperator will be (script, text) dependent!!
	return regex.split(seperator, text)

								
def charecterSet(script="latin1"):
## not clear if to pass as language name(english, hindi) or script(latin1, devanagri) 
	literals = "";
	if script == "latin1":
		literals = 'abcdefghijklmnopqrstuvwxyz'
	elif script == "devanagari":
		for i in range(0x0900, 0x094F):
			literals += chr(i)
	
	return literals


def readBook(book, inPath, lineProcess=False):
	str="/"
	f = open(str.join((inPath, book)), encoding='utf-8')
	lines = f.read()

	## Here lies the problem!! as each book has not so definite raw-data processing
	if lineProcess == True:
		return removeSChars(lines)
	return lines
