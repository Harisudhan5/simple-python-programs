from re import I


print("PROGRAM TO CHECK WHETHER THE GIVEN NUMBER IS PERFECT NUMBER OR NOT")
n=int(input("Enter a number : "))
sum=0
t=n
i=1
while(i<n):
    if(n%i==0):
        sum=sum+i
    i=i+1
if(t==sum):
    print("The number is a Perfect Number")
else:
    print("The number is not a Perfect Number")


