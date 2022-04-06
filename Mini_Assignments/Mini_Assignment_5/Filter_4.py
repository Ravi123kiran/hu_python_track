from functools import reduce

lst1=[5,5,2]
result=reduce((lambda x,y:x*y),lst1)

print(result)

