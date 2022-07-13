print("PROGRAM TO CHECK WHETHER THE NUMBER IS ARMSTRONG NUMBER")
n=int(input("Enter a number : "))
temp=n
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem**3
    n=n//10
if(temp==sum):
    print("The given number is armstrong number")
else:
    print("The given number is not a armstrong number")
