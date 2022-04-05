input = int(input('Input number of rows: '))
n = 0
row = []
while n < input:
    m = 11 ** n
    k=len(str(m))
    for p in range(input-k):
        m=m*10
    row.append(m)
    n += 1
for i in range(0,len(row)):
    row[i] = str(row[i])
    print(row[i])
