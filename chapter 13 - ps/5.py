from functools import reduce
l = [2,3,212,345,4,3,222]

def greater(a,b):
    if(a>b):
        return a 
    return b


print(reduce(greater, l))