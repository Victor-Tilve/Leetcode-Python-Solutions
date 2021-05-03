
##..---------------------------------------

##Hash table

nums = [3,5,4,3,5,8]
# key [hash(value) for _,value in enumerate(nums)]
key =[hash(value) for _,value in enumerate(nums)]
hash = {k:v for k, v in zip(key, nums)}
# print(type(key))
# print(len(hash))

##..---------------------------------------

test = {'a':5,'b':6}
test['b'] = 6
print(len(test))