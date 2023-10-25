# Polymorphism
# Function/Method overloading is achieved by passing *args where we can have any number of parms passed
class ADD:
    def sum(self, a = None, b = None, c = None):        
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s
       
s = ADD()

# sum of 1 integer
print(s.sum(1))
# sum of 2 integers
print(s.sum(3, 5))
# sum of 3 integers
print(s.sum(1, 2, 3))

# Operator Overloading in Python. To overload '+' operator use __add__ method in your class definition
class Student:
   
    # defining init method for class
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
 
    # overloading the + operator
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3
 
s1 = Student(58, 59)
s2 = Student(60, 65)
s3 = s1 + s2
print(s3.m1, s3.m2)
print(s3)
print(type(s3))

# Encapuslation 
# Is achieved by defining a Class and all its Data and Method inside it.

# Inheritence
# The Class definition has the Parent Class as its parameter
# Function/Method overriding - defining the method with the same name in the child class as well
# parent class
class Programming:
   
    # properties
    DataStructures = True
    Algorithms = True
     
    # function practice
    def practice(self):
        print("Practice makes a man perfect")
     
    # function consistency
    def consistency(self):
        print("Hard work along with consistency can defeat Talent 1.")
         
# child class       
class Python(Programming):
     
    # function
    def consistency(self):
        print("Hard work along with consistency can defeat Talent 2.")

Py = Python()
Py.consistency()
Py.practice()

# Abstraction - Gives a template of methods within the class and these classes are defined in the child classes
# Python does not directly support it, but uses something called Abstract Base Class (ABC) and using the decorator @abstractmethod
# Python program showing abstract base class work
from abc import ABC, abstractmethod
# The actual Parent Class within the Program is actually a Sub-Class of ABC where abstractmethod is defined as well
class Polygon(ABC):
	@abstractmethod
	def noofsides(self):
		pass

class Triangle(Polygon):
	# overriding abstract method
	def noofsides(self):
		print("I have 3 sides")

class Pentagon(Polygon):
	# overriding abstract method
	def noofsides(self):
		print("I have 5 sides")

class Hexagon(Polygon):
	# overriding abstract method
	def noofsides(self):
		print("I have 6 sides")

class Quadrilateral(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 4 sides")

# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()
