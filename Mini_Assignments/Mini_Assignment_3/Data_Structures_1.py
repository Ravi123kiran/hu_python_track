lis=[[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]

for i in range(len(lis)):
    d={}
    for j in range(len(lis[i])):
        d[lis[i][j]]=d.get(lis[i][j],0)+1
    k=list(d.values())
    m=list(d.keys())
    for i in range(len(k)):
        if k[i]>=2:
            print(m[i],'->',k[i])

