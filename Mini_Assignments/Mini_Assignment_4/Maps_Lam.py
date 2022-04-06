lst=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
counting_A=list(map(lambda x:x.count("A"),lst))
counting_a=list(map(lambda x:x.count("a"),lst))
comb=list(map(lambda x,y:[x,y],counting_A,counting_a))
print(comb)
