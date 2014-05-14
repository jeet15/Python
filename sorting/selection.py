#!usr/bin/python
class Selection(object):
    '''
    Summary of the  selection_sort
    '''
    def selection_sort(self,a):                        #declaring the function
        i = 0                                          #declaring the varaible
        l = len(a)                                     #length of the array
        min = 0                                        #mininmum variable for division of the list 
        for i in range(l):
            min = i                                    #assume the the first value is minimum
            for j in range(i+1,l):                     
                if a[j] < a[min]:                      # check the condition with next value
                    a[j],a[min] = a[min],a[j]          # swap
        return a
        

s = Selection()                                        # making the class object
d = [7,1,9,0,2,16,22]
print s.selection_sort(d)
