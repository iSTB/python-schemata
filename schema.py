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

	def __str__(self):
		return self.string

	def __repr__(self):
		return "Schema: + " self.string

	
	def get_length(self):
		return len(self.string)	


	def get_anti_order(self):
		return self.string.count('*')


	def get_def_length(self):
		#TODO write this.
		return -1			

	def get_order(self):
		return self.get_length() - self.get_anti_order()

	def set_string(self,string):
		self.string = string 

		


class schemata(self,schemata=[],alphabet=[])

	
	def expansion(self):
		
		


 
