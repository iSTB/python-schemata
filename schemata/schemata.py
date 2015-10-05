__author__ = "Jack McKay Fletcher"
__copyright__ = "Copyright 2015, Plymouth University "
__credits__ = ["Thomas Wenneker"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Jack McKay Fletcher"
__email__ = "jack.mckayfletcher@plymouth.ac.uk"
__status__ = "Production"


"""
This file  contains the schema class and functions over schema such as join, meet and complete.
"""

gp = True
try:
    from graphviz import Graph
except ImportError:
    gp = False   
 
class schema(object):

    """
    The schema class.
    """
    def __init__(self, string=''):

        if type(string) == type(self):
            self.string = string.string
            self.alphabet = string.alphabet 
            
        else:
            self.string = string
            self.alphabet = []

    def __str__(self):

        if self.string == '':
            return "e"

        return self.string

    def __repr__(self):

        if self.string == '':
            return "e"

        return self.string

    def __getitem__(self, index):

        return self.string[index]

    def __len__(self):

        return len(self.string)

    def __ge__(self, other):

        if type(other) != type(self) and type(other) != str:
            raise TypeError("Cannot call >= on type " + str(type(self)) +
                            " and " + str(type(other)))

        return join(self, other) == self

    def __gt__(self,other):
        
        if type(other) != type(self) and type(other) != str:
            raise TypeError("Cannot call >= on type " + str(type(self)) +
                            " and " + str(type(other)))
        return self.__ge__(other) and self != other


    def __le__(self, other):

        if type(other) != type(self) and type(other) != str:
            raise TypeError("Cannot call <= on type " + str(type(self)) +
                            " and " + str(type(other)))

        return meet(self, other) == self


    def __lt__(self,other):
        
        if type(other) != type(self) and type(other) != str:
            raise TypeError("Cannot call >= on type " + str(type(self)) +
                            " and " + str(type(other)))
        
        return self.__le__(other) and self != other

    def __eq__(self, other):

        if type(other) != type(self) and type(other) != str:
            raise TypeError("Cannot call == on type " + str(type(self)) +
                            " and " + str(type(other)))

        if type(other) == str:
            return self.string == other
        return self.string == other.string


    def __ne__(self,other):
        if type(other) != type(self) and type(other) != str:
            raise TypeError("Cannot call == on type " + str(type(self)) +
                            " and " + str(type(other)))
        if type(other) == str:
            return self.string != other
        return self.string != other.string

    def __cmp__(self,other):
            if self == other:
                return 0
            if self < other:
                return -1
            if self > other:
                return 1


    def __nonzero__(self):
        """
        A schema is nonzero when it is not the empty schema
        """

        if self.string == '':
            return False
        return True

    def is_empty_schema(self):
        """
        Returns true if this schema is the empty schema.
        """

        if self.string == '':
            return True
            
        else:
            return False 

    def get_anti_order(self):

        """
        Returns the anti order of the current schema. The anti-order is the
        number of wild cards (*'s) in the schema

        Example:

        >>> s = schema('1**0**')
        >>> s.get_anti_order()
        >>> 4
        """
        return self.string.count('*')

    def get_defining_length(self):
        """
        Returns the defining length of the schema.
        The defining length is the distance between the first
        and last fixed symbol.

        Example:        
        >>> s = schema('1**0**')
        >>> s.get_defining_length(s)
        >>> 3
        """

        start = 0
        last = 0

        for i in range(len(self)):
            if self[i] != '*':
                start = i
                break

        for i in reversed(range(len(self))):
            if self[i] != '*':
                last = i
                break
        return last - start

    def get_top(self):
        """
        Returns the maximal possible element assosiated with this schema.
        
        Example:
        
        >>> s = schema.('1***10')
        >>> s.get_top()
        >>> s.get_top()
        >>> ***
        """
        top = ''
        for i in xrange(len(self)):
            top += '*'

        return top

    def get_order(self):
        """
        Returns the order of the current schema.

        Example:

        >>> s = schema('1***10')
        >>> s.get_order()
        >>> 3
        """

        return len(self) - self.get_anti_order()

    def set_string(self, string):
        """
        Sets the schema. This can only take a string as input. 
        """


        if type(x) != str:
            raise ValueError("set_string() must take a str as input")

        self.string = string 

    def set_alphabet(self, alpha):
        """
        Sets the alphabet used by the schema. Alpha can only be a list 
        of strings.

        Example:

        >>> s = schema('1***10')
        >>> s.set_alphabet(['1','0'])
        >>> 3

        """
 
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
        >>> s = schemata.schema('1*0')
        >>> s.set_alphabet(['1','0'])
        >>> s.expansion()
        >>> ['110','101']
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


def __to_schema(xs):
    """
    Turns a list of strings into a list of schema.
    """

    if type(xs) == str:
            return schema(xs)

    schem = schema()

    if type(xs) == list:
        new = []
        for x in xs:
            if type(x) == type(schem):
                new.append(x)

            else:
                new.append(schema(x))

    return new


def join(s1,s2):
    """
    Returns the join of schema s1 and s2.  
    """
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

def supremum(xs):

    if xs  == []:
        return schema()
    current = xs[0]
    for string in xs:
        current = join(current,string)
    
    return current

def infimum(xs):

    if xs == []:
        return schema()

    current = xs[0]

    for string in xs:
        current = meet(current,string)

    return current

def complete(base):
    """
    Returns the schematic completion of the set base.
    
    That is, for a given set of words of the the same length, base, returns:

    {supremum(X) | X \subseteq base} 

    """
    return __to_schema(__complete(base))

def __complete(base):
    new = []

    for i in base:
        for j in base:
            if i != j:
                x = join(i,j)
                if x not in base+new:
                    new.append(x)
    #for pair in itertools.product(base, repeat=2):
    #    if pair[0] != pair[1]:
    #        j = join(pair[0],pair[1])
    #        if j not in base+new:
    #            new.append(j)
    if new == []:
        return base + ['']

    else: return base+complete(new)


def is_lower_n(s1,s2,xs):
    """
    Returns true if schema s1 is a lower neighbour of schema s2 in set of schema xs
    """ 
    if __check_type(s1) != True:
        raise ValueError(str(s1) + " not of type string or schema")
    
    if __check_type(s2) != True:
        raise ValueError(str(s2) + " not of type string or schema")

    if s1 not in xs or s2 not in xs:
            
        raise ValueError("given inputs not in given set")

    if type(s1) == str:
        s1 = schema(s1)

    if type(s2) == str:
        s2 = schema(s2)

    
    xs = __to_schema(xs)

    if ((s1 <= s2) == False) and ((s2 <= s1)==False):
        return False #Case when s1 and s2 are not compareable

    if s1 >= s2:
        return False #When s1 is bigger than s2 then s1 cannot be a lower neighbour of s2


    new = [x for x in xs if x != s1 and x != s2]
    print new    
    for i in new:
        if i >= s1 and i <= s2: 
            return False
            break

    return True

def comparable(s1,s2):

    if ((s1 <= s2) == False) and ((s2 <= s1)==False):
        return False #Case when s1 and s2 are not compareable

    return True

def get_lower_ns(s,ss):
    """
    Gets all lower neighbours of s in ss
    """
    if __check_type(s) != True:
        raise ValueError(str(s) + " not of type string or schema")
    

    if type(s) == str:
        s = schema(s)

    #gets the set of lower neighbours of y in xs.
    lns = []
    for s1 in ss:
        if is_lower_n(s1,s,ss):
            lns.append(s1)
        
    return lns

        
def draw(ss,filename):
    """
    Draws the hasse diagram of ss. Saves diagram in the file filename as a pdf.
    """
    if not gp:
        raise ImportError("graphviz not installed cannot draw. Use sudo pip install graphviz to enable drawing")
    
    dot = Graph()

    for s in ss:
        dot.node(str(s),str(s))

    for s in ss:
        ln = get_lower_ns(s,ss)
        for l in ln:
            dot.edge(str(s),str(l))

    dot.render(filename)
    return dot.source
