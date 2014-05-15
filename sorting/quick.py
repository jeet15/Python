#!/usr/bin/python
class Quick(object):
    ''' summary of the quick sort algorithim
    '''
    def partition(self,l):
        length = len(l)                                         #declarationlength of the list
        pivot =  l[length-1]                                    # declare a pivot variable for division of the list
        left = []
        right = []
        for i in range(length-1):                               #cout till the length-1
            pos = l[i]                                          # declare the postion of the value
            if pos <= pivot:                                    # check the condition of position to pivot value
                left += [pos]                                   # add the value to left
            else:
                right += [pos]                                  # add the value to right
        return (left, pivot, right)
    ''' summary of the function of the quick sort
    '''
    def quick_sort(self,a):
     #base class   
        if len(a) <= 1:                                         # check wheather the list have the element 
            return a
      # recursive      
        else:
            #divide
            (left, pivot, right) = self.partition(a)            # divide the list according to the algorithim
            #conqure the list
            sorted_left = self.quick_sort(left)                 #sort the element of the left
            sorted_right = self.quick_sort(right)               #sort the element of the right
            # combine the list
            return sorted_left + [pivot] + sorted_right         # join the complete list
  
  #make the object of class and call the function
  

k = Quick()
d = [9,2,-1,22,13,61]
print k.quick_sort(d)
