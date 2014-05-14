#!/usr/bin/python

class Person(object):
    ''' Summmary of a person details'''

    name = "No name yet"
    age = 0
 
    # methods
    def setName(self, name):
        self.name = name
 
    def setAge(self, age):
        self.age = age
 
    def talk(self):
        print("Hi! My name is", self.name, "and I am", self.age, "years old.")

p=person()      
print p.setName('Gurjeet')
print p.setAge(25)
print p.talk()
