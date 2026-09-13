n= int(input("enter the number number:"))
a=[]
for i in range(2,n+1):
    if n%i==0:
       a.append(i)
a.sort()
print("the smalest divisor is :",a[0])
