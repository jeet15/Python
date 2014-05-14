#!usr/bin/python
class Insertion(object):
    def insertion_sort(self,a):
        i = 1
        l = len(a)
        k = 0
        for i in range(l):
            k = a[i]
            j = i - 1
            while (j >= 0) and (a[j] > k):
                a[j+1] = a[j]
                j = j - 1
                a[j+1] = k


            

h = Insertion()
s = [30,70,80,20,10]
print h.insertion_sort(s)