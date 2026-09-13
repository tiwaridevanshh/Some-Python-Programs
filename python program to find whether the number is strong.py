print("enter the number to be checked :")
num = int(input())
sum1=0
temp = num
while(num):
    f=1
    i=1
    r=num%10
    while(i<=r):
        f= f*i
        i=i+1
    sum1=sum1+f
    num=num//10
if(temp==sum1):
    print("the number is a strong number")
else:
    print("the number is not a strong number")
