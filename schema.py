__author__ = "Jack Fletcher"
__copyright__ = "Copyright 2015, Plymouth University "
__credits__ = ["Thomas Wenneker"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Jack Fletcher"
__email__ = "jack.mckayfletcher@plymouth.ac.uk"
__status__ = "Production"


class schema(object):
	def __init__(self, string = '', alphabet=[]):
		self.string = string
		self.alphabet = alphabet
	
	def get_length(self):
		return len(self.string)	


	def get_anti_order(self):
		return self.string.count('*')


	def get_order(self)
		return self.get_length() - self.get_anti_order()
	

 
