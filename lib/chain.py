import random

class Chain():
	def __init__(self, corpus, index):
		self.corpus = corpus	
		self.index = index
	def next(self):	
		# Filter out sentence ends unless it's the only option
		conts = []
		for x in self.corpus[self.index]:
			if x.find('.') > -1:
				pass
			else:
				conts.append(x)
		if len(conts) == 0:
			print('conts ended up empty...sadface')
			conts = self.corpus[self.index]
		# Temporary structure for MVP...should end sentence if it reaches a KeyError
		# TODO: Make this less ugly!!! IT IS GROSS!!!!!
		futile = False
		check = 0
		while not futile:
			try:
				current = self.index
				rand = random.randint(0, len(conts)-1)
				self.index = (current[1], conts[rand])
				return conts[rand]
			except KeyError:
				pass
			finally:
				check += 1
				if check == 10:
					futile = True
					return ''
	def end(self):
		ends = []
		for x in self.corpus[self.index]:
			if x.find('.') > -1:
				ends.append(x)	
		if len(ends) == 0:
			ends = self.corpus[self.index]
		current = self.index
		rand = random.randint(0, len(ends)-1)
		self.index = (current[1], ends[rand])
		return ends[rand]
