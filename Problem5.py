# def random1():
#     import random
#     i=0
#     while i < 100:
#         b = random.randint(10, 50)
#         print(b)
#         i+=1
# random1()


# import random

# def decorforlist(func):
#     def inner():
#         a = set(func())
#         return list(a)
#     return inner    


# @decorforlist
# def listGen():
#     somelist = [random.randint(10, 50) for x in random(100)]
#     return somelist

# print(listGen())

import random
def decorforlist(func):
    def inner():
        s = set(func())
        return list(s)
    return inner

@decorforlist
def listGen(): 
    somelist = [random.randint(10, 50) for x in range(100)]
    return somelist
  
print(listGen())

