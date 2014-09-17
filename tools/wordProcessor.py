import regex, pkgutil
import hashlib


class WordProcessor:

	def removeNLine(self, line):
		"""
		remove new line char from line
		"""
		return regex.sub(r"(\n)", r"", line)


	def removeSChars(self, line):
		"""
		remove special(specific) chars(sChars provided in list) from line
		"""
		sChars = [r"\,", r"\!", r"\?", r"\:", r"\;", r"\(", r"\)", chr(0x0964), chr(0x0965), chr(0x097D)]
		for char in sChars:
			line = regex.sub(char, r"", line)
		return line
							
	def wordsInText(self, text, literals, seperator="\s+"):
		"""
		returns list of tokens(words) in text
		Word seperator will be (script, text) dependent!!
		#return regex.split(seperator, text.lower())
		"""
		#return regex.findall(r"\w+", text.lower())
		return regex.findall(r"\w+", text, flags=regex.IGNORECASE)

								
	def charecterSet(self, script="english"):
		"""
		returns literals for script(english, hindi)
		set all to unicode
		"""

		literals = "";
		if script == "english":
			literals = 'abcdefghijklmnopqrstuvwxyz'
		elif script == "hindi":
			for i in range(0x0900, 0x094F):
				literals += chr(i)
	
		return literals


	def readBook(self, datapkg, book):
		"""
		returns data after reading
		datapkg:
		book:
		"""
		try:
			data = pkgutil.get_data(datapkg, book)
		except Exception as e:
			print(" :( **** Error raised *** ); ")
			print("Reason: ", e)

		## md5 hash for text read
		## could be helpful to assertain integrity of corpus data, and need only be reread(corpus) if hashMd5 changed in certain cases  
		m = hashlib.md5()
		m.update(data)
##		print("Hash digest if file ", m.hexdigest())

		return data.decode()
