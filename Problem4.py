# a = [1, 1, 1, 1, 1, 1,]

# def destr_array(array):
# 	if len(array) > 1:
# 		array.pop(-1)
# 		destr_array(array)

# print(destr_array(a))		



def set_deletion(st):
    if st:
        st.pop()
        print(st)
        set_deletion(st)

simple_set = {10, 20, 30, 40, 123, 434, 10}
print(simple_set)
set_deletion(simple_set)