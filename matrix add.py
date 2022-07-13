print("PROGRAM TO CALCULATE MATRIX ADDITION")
a=[]
b=[]
c=[]
row=int(input("Enter the row of the matrix : "))
col=int(input(" Enter the column of the matrix : "))

print("Enter the elements of first matrix : ")
for i in range(row):
    a.append([])
    for j in range(col):
        a[i].append(int(input()))
        

print("Enter the elements of the second matrix : ")
for i in range(row):
    b.append([])
    for j in range(col):
        b[i].append(int(input()))

for i in range(row):
    c.append([])
    for j in range(col):
        c[i].append(a[i][j]+b[i][j])

print("THE ADDITION OF TWO MATRIX IS : ")
for i in range(row):
    print(c[i])