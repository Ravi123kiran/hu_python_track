lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]
negative=list(filter(lambda x :x<0,lst1))
res=list(map(lambda x:abs(x),negative))

print("Negetive numbers are:",res)

