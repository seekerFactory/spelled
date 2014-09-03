import regex, pkgutil


class WordProcessor:

	def removeNLine(self, line):
		return regex.sub(r"(\n)", r"", line)


## just a thought !# could be something not in literals list(including pause and small pause) will be easier to check.
	def removeSChars(self, line):
## will seperate sChars and pass name, as param,  to be removed 
	#sChars = [r"(\,)", r"(\!)", r"(\?)", r"(\:)", r"(\;)", r"(\()", r"(\))", chr(0x0964), chr(0x0965), chr(0x097D)]
		sChars = [r"\,", r"\!", r"\?", r"\:", r"\;", r"\(", r"\)", chr(0x0964), chr(0x0965), chr(0x097D)]
		for char in sChars:
			line = regex.sub(char, r"", line)
		return line
							
	def wordsInText(self, text, literals, seperator="\s+"):
	## Word seperator will be (script, text) dependent!!
	#return regex.split(seperator, text.lower())
		return regex.findall(r"\w+", text.lower())

								
	def charecterSet(self, script="english"):
## unicode set for hindi

		literals = "";
		if script == "english":
			literals = 'abcdefghijklmnopqrstuvwxyz'
		elif script == "hindi":
			for i in range(0x0900, 0x094F):
				literals += chr(i)
	
		return literals


#	def readBook(self, book, inPath, lineProcess=False):
#		str="/"
#		f = open(str.join((inPath, book)), encoding='utf-8')
#		lines = f.read()

	## Here lies the problem!! as each book has not so definite raw-data processing
#		if lineProcess == True:
#			return self.removeSChars(lines)
#		return lines

	def readBook(self, datapkg, book):

		data = pkgutil.get_data(datapkg, book)
		return data.decode()
