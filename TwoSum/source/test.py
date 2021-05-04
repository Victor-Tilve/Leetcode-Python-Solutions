
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

for key in test:
    print(f'key: {key}')

# hash = {k:v for i,(k,v) in enumerate(zip(hash(nums),nums))}
# hash = {k:v for k,v in zip(hash(nums),nums)}
# b = [k for k,v in zip(hash(nums),nums)]

b = {hash(value): [value,i] for i,value in enumerate(nums)}

# print(hash)