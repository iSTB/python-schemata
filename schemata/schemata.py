__author__ = "Jack McKay Fletcher"
__copyright__ = "Copyright 2015, Plymouth University "
__credits__ = ["Thomas Wenneker"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Jack McKay Fletcher"
__email__ = "jack.mckayfletcher@plymouth.ac.uk"
__status__ = "Production"
import itertools

try:
    import networkx as nx
except ImportError:
    raise ImportError("networkx not installed on this machine. To enable "
                      "drawing functionality for this package, "
                      "please install networkx.")


class schema(object):

    """
    The schema class
    """
    def __init__(self, string=''):

        self.string = string
        self.alphabet = []

    def __str__(self):

        if self.string == '':
            return "''"

        return self.string

    def __repr__(self):

        if self.string == '':
            return "''"

        return self.string

    def __getitem__(self, index):

        return self.string[index]

    def __len__(self):

        return len(self.string)

    def __ge__(self,other):

        if type(other) != type(self) and type(other) != str :
            raise TypeError("Cannot call >= on type " + str(type(self)) +" and " + str(type(other)))
        
        return join(self,other) == self


    def __le__(self,other):
        
        if type(other) != type(self) and type(other) != str :
            raise TypeError("Cannot call <= on type " + str(type(self)) +" and " + str(type(other)))
        
        return meet(self,other) == self


    def __eq__(self,other):


        if type(other) != type(self) and type(other) != str :
            raise TypeError("Cannot call == on type " + str(type(self)) +" and " + str(type(other)))
        
        if type(other) == str:
            return self.string == other
        return self.string == other.string 
    
    def get_anti_order(self):
        return self.string.count('*')

    def get_def_length(self):
        #TODO write this.
        return -1           

    def get_order(self):
        return self.get_length() - self.get_anti_order()

    def set_string(self,string):

        if type(x) != str:
            raise ValueError("set_string() must take a str as input")

        self.string = string 

    def set_alphabet(self,alpha):
        if type(alpha) != list:
            raise ValueError("set_alphabet only can take be a list of chars or strings as inputs" ) 

        for char in alpha:
            if type(char) != str:       
                raise ValueError("set_alphabet only can take be a list of chars or strings as inputs" ) 


        self.alphabet = alpha


    def expansion(self):
        """ 
        Expands the schema.
        Note: The alphabet of the schema needs to be set first, use set_alphabet().

        Example:
        >>>s = schemata.schema('1*0')
        >>>s.set_alphabet(['1','0'])
        >>>s.expansion()
        >>>['110','101']
        """
        
        if self.alphabet == []:
            raise ValueError('exansion() cannot be called when the alphabet not set, use set_alphabet()')
            return None

        expanded_set = []
            

def __all_eq_lens(xs):
    """
    Checks if all items in a list are of the same length.

    Keyword arguments:

    xs -- a list whose elements are of the same type and have the method len()  
    """

    if len(xs) == 0:
        raise ValueError("__all_eq_lens() cannot be called on the empty list")

    list_type = type(xs[0])
    same_type = True

    for x in xs:
        if type(x) != list_type:
            same_type = False
            break 

    if same_type == False:
        raise ValueError("__all_eq_lens() can only be called on a list whose elements are of the same type")

    try:
        len(xs[0])
    except Exception:
        raise ValueError("__all_eq_lens() can only be called on a list whose elements have len()")


    if len(xs) == 1:
        return True
    
    lens = map(len,xs)
    first = lens[0]

    all_eq = True

    for l in lens:
        if l != first:
            all_eq = False
            break
    return all_eq


def __check_type(x):
    """
    Checks if a variable x is of type schema or string.
    """

    s = schema()

    if type(x) == type(s) or type(x) == str:
        return True

    return False


def join(s1,s2):    
    if __check_type(s1) != True:
        raise ValueError(str(s1) + " not of type string or schema")
    
    if __check_type(s2) != True:
        raise ValueError(str(s2) + " not of type string or schema")

    if type(s1) == str:
        s1 = schema(s1)

    if type(s2) == str:
        s2 = schema(s2)


    if s1  == s2:
        return s1

    if s1  == '':
        return s2
    if s2  == '':
        return s1
    
    if len(s1) != len(s2):
        raise ValueError("join can only be performed on schema or strings of the same length")


    new = ''

    for i in xrange(len(s1)):
        if s1[i] == s2[i]:
            new +=s1[i] 
        else:
            new+='*'
    return schema(new)  


def meet(s1,s2):

    if __check_type(s1) != True:
        raise ValueError(str(s1) + " not of type string or schema")
    
    if __check_type(s2) != True:
        raise ValueError(str(s2) + " not of type string or schema")

    if type(s1) == str:
        s1 = schema(s1)

    if type(s2) == str:
        s2 = schema(s2)


    if s1 == s2:
        return s1
    if s1== '':
        return s1

    if s2 == '':
        return s2

    if len(s1) != len(s2): 
        raise ValueError("join can only be performed on schema or strings of the same length")
    new = ''
    for i in xrange(len(s1)):
        if s1[i] == s2[i]:
            new +=s1[i]
        else: 
            if s1[i] == '*' and s2[i] != '*':
                new += s2[i]
            if s2[i] == '*' and s1[i] !='*':
                new += s1[i]

    if len(new) != len(s1):
            return schema()
    return schema(new)



def complete(base):
    new = []
    for pair in itertools.product(base, repeat=2):
        if pair[0] != pair[1]:
            j = join(pair[0],pair[1])
            if j not in base+new:
                new.append(j)
    if new == []:
        return base + ['']

    else: return base+complete(new)


    
 
