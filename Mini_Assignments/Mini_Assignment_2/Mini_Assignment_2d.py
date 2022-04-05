n_rows= int(input("enter no of rows:"))

for row in range(1,n_rows+1):
    for col in range(1,n_rows+1):
        if(col == n_rows) or (row == 1) or (col == row):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
