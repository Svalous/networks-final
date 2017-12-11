import os
import re
import chain as mark

class Generator():
	def __init__(self, file):
		self.file = file 
		self.sentence = ''
		self.chain = None
	def makeChain(self):
		try:
			f = open(self.file, 'r')
			lines = f.read()
			lines = re.sub(r'\n', r' ', lines)
			lineArr = lines.split(' ')
			lineArr = [x for x in lineArr if x != '']
			corpus = {}
			for x in range(0, len(lineArr) - 2):
				x0 = lineArr[x]
				x1 = lineArr[x+1]
				x2 = lineArr[x+2]
				try:
					corpus[(x0,x1)].append(x2)
				except KeyError:
					corpus[(x0,x1)] = [x2]
			self.chain = mark.Chain(corpus, list(corpus.keys())[0])
		except Exception:
			raise
		finally:
			f.close()
	def makeSentence(self, minLength):
		# TODO: Below should go to n - (avg time to .) or something more optimal
		# Perhaps look down the line one iteration to ensure that the sentence ends on time
		for x in range(0, minLength-1):
			self.sentence += self.chain.next() + ' '
		check = 0
		futile = False
		MAX_CHECK = 100
		# TODO: Make this loop not gross!  SO ICKY!!
		while not futile:
			self.sentence += self.chain.end()
			if self.sentence.find('.', len(self.sentence)-2) > -1:
				check = MAX_CHECK
			else:
				self.sentence += ' '
			check += 1
			if check >= MAX_CHECK:
				futile = True		
		return self.sentence
