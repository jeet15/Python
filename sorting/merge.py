#!usr\bin\python
class Merge(object):
    '''summar of the list divida a list
    '''
    def merging(self, list1, list2):                   #using the algo with recursion
        output = []                                    # declaration of output as empty list
        i = 0
        j = 0
        length1 = len(list1)                           #divide a list into two parts
        length2 = len(list2)
        while (i < length1) or (j < length2):          # check the condition with while loop
        #case1: when both the list have numbers
            if i < length1 and j < length2:            # condition of checking length of list 1 and 2
                if list1[i] < list2[j]:
                    output += [list1[i]]               # adding the value in the output
                    i = i+1
                else:
                    output += [list2[j]]
                    j = j+1
            # case2: when 1st list have the numbers        
            elif i < length1:
                output += [list1[i]]
                i = i+1
            # case3: when the 2nd list have the numbers    
            else:
                output += [list2[j]]
                j = j+1
        return output                                   #return the value output


    def merge_sort(self, l):
        # chack the base class
        length = len(l)
        if length <=1:
            return l
        else:
        #recursive 
        #divide
            mid = length/2                             #divide the list in two parts
            left = l[0:mid] 
            right = l[mid:]
        #conqure the list
            sorted_left = self.merge_sort(left)
            sorted_right = self.merge_sort(right)
        #combine the list
            return self.merging(sorted_left,sorted_right)

'''call the class
'''
m = Merge()
print m.merge_sort([10,0,80,9,-3,77,15,33,21,9,5,88])