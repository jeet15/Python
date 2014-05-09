#!usr/bin/python
class Binary():

        '''first diclare a boolean variable '''

        FOUND = False
         
               #Delclaration of algo of binary search'''


        def binarySearch(self, i, list, lb, ub):
                if ub < lb:
                        return self.FOUND
 
                mid = (lb + ub) / 2
                if list > i[mid]:
                        return self.binarySearch(i, list, mid + 1, ub)
                elif list < i[mid]:
                        return self.binarySearch(i, list, lb, mid - 1)
                else:
                        return mid
 
        def search(self, i, list):
                lb = 0
                ub = len(i) - 1
                return self.binarySearch(i, list, lb, ub)
 
bs = Binary()
a = [1, 2, 3, 5, 9, 11, 15, 66]

#call the function of binary search
print bs.search(a, 11)