#Version: Python 3.9
#Description: This program will display the pets name, type of animal, and pets age while storing and displaying data. 

_name=''

_animal_type='Cat'

_age=0

def _init_(n,t,ag):

_name =n

_animal_type = t

_age=ag

def set_name(n):

_name=n

def set_animal_type(t):

_animal_type=t

def set_age(ag):

_age=ag

def get_name():

return _name

def get_animal_type():

return _animal_type

def get_age():

return _age

def main():

x=Pet()

x.set_name('Mr Pickle')

x.set_animal_type('Cat')

x.set_age(4)