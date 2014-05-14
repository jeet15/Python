#!urs/bin/python
class Bubble(object):
    def bubble_sort(self, a):
        i = 0
        l = len(a)
        for i in range(l):

            for j in range(i+1,l):
                if a[i] > a[j]:
                    a[i],a[j] = a[j],a[i]
                
        return a
                    

    #def fun(self, j):
     #   return self.bubble_sort(j)


b = Bubble()
j = [1,5,6,2,0,17]
print b.bubble_sort(j)


