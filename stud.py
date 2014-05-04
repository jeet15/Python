#!/usr/bin/python

class Student(object):
      
    def __init__(self, fname,lname,class_section,rollno,age,address):

        self.fname = fname
        self.lname = lname
        self.class_section = class_section
        self.rollno = rollno
        self.age = age
        self.address = address


      
    def  get_result(self):


        return ' %s %s %s %s %s (%s)' %(self.fname,self.lname,self.class_section,self.rollno,self.age,self.address)    

   

        
p = Student('Gurjeet','Singh','XII_A','A42',15,'Milan_Vihar_Moradabad')
print p.get_result()