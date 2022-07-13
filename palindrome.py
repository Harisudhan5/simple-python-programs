print("PROGRAM TO FIND WHETHER THE GIVEN NUMBER IS PALINDROME OR NOT")
num=int(input("Enter a number : "))
zem=num
sum=0
while(num>0):
    rem=num%10
    sum=sum*10+rem
    num=num//10
if(zem==sum):
    print("The number is palindrome")
else:
    print("The number is not a palindrome")
