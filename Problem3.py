# def rec(x):
# 	print(x)
# 	rec(x -1)

# rec(-1)	

from random import randint

def rec_even(num):
    
    if num > 0:
        print(randint(0, 499) * 2 + 1, end=' ')
        rec_even(num-1)
    else:
    	print()

rec_even(10)