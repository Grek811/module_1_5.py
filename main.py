immutable_var = 1,2,3,4,5,6,7,8,9,0
print(immutable_var)
immutable_var = ([1,2,3],4,5,6,7,8,9,0)
print(immutable_var)
immutable_var[0][0] = 2
print(immutable_var)
mutable_list = ["apple", "coconut", "banana",1,2,3,4,5,6,7,8,9,0]
print(mutable_list[0])
mutable_list[0] = "peach"
print(mutable_list)