#!/usr/bin/python
class Person(object):


    '''Summary of the person'''   

    def __init__(self,first_name,last_name,age):
    	self.first_name = first_name 
        self.last_name = last_name
        self.age = age

    def  get_result(self):
    	return ' %s %s (%s)' %(self.first_name,self.last_name,self.age)
       	
class Employee(Person):
	def __init__(self,first_name,last_name,age,salary):
		super(Employee,self).__init__(first_name,last_name,age)
		self.salary=salary
		
		


p=Employee('Gurjeet','Singh',24,10000)

print p.get_result()
print p.salary

