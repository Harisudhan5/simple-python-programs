a=int(input("Enter a numer : "))
b=int(input("Enter a number : "))
while(b!=0):
    sm=a&b
    a=a^b
    b=sm<<1
print(a)



