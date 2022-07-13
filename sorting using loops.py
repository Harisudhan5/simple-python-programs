#python program to sort an array of numbers using loops
list=[]
len=int(input("Enter the length of string :"))
for i in range(0,len):
    list.append(int(input("Enter a value : ")))
print("-------------------------------------")
print("Before sorting : ")
print(list)

for i in range(0,len):
    for j in range(i+1,len):
        if(list[i]>list[j]):
           list[i],list[j]=list[j],list[i]
print("---------------------------------------")
print("After sorting :")

print(list)