# def rec(x):
# 	print(x)
# 	rec(x+1)

# rec(1)

# def rec(x):
# 	if x < 4:
# 		print(x)
# 		rec(x+1)
# 		print(x)

# rec(1)

# def sumN(n1, n2):
# 	print(n1 + n2)

# sumN(1, 2)

# 
# a = (lambda n1, n2: n1 + n2)(1, 2)
# print(a)



# a = (lambda n1, n2: if n1 == 1: return 'hello' else: for i in range(10): return i

#  print(a)

# def sumN(n1, n2):
# 	print(n1 + n2)

# sumN(1, 2)

# a = (lambda n1: True if (n1 == 1) else False)(1)
# print(a)

# def sumN(n1, n2):
#  	print(n1 + n2)

# sumN(1, 2)

#  a = lambda n1: n1**2 if n1 < 10 else(n1**3 if n1 < 20 else n1)
# print(a(12))




# from datetime import datetime

# def iter():
# 	l = []
# 	for i in range(10000):
# 		if i % 2 == 0:
# 			l.append(i)
# 	return l
			

# def gen():
# 	l = [x for x in range(10000) if x % 2 == 0]
# 	print(datetime.now() - start)

# 	return l

# iterr()
# gen()



# from datetime import datetime
#   2 
#   3 def timefix(func):
#   4     def wrapper():
#   5         start = datetime.now()
#   6         result = func()
#   7         print(datetime.now() - start)
#   8         return result
#   9     return wrapper
#  10 
#  11 @timefix
#  12 def iterr():
#  13     #start = datetime.now()
#  14     l = []
#  15     for i in range(10000):
#  16         if i % 2 == 0:
#  17             l.append(i)
#  18     #print(datetime.now() - start)
#  19     return l
#  20 
#  21 @timefix
#  22 def gen():
#  23     #start = datetime.now()
#  24     l = [x for x in range(10000) if x % 2 == 0]
#  25     #print(datetime.now() - start)
#  26     return l
#  27 
#  28 iterr()
#  29 gen()














