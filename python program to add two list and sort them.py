n1= int(input("Enter the number of elements to be inserted:"))
a=[]
for i in range(0,n1+1):
    b=int(input("Enter the element:"))
    a.append(b)
n2= int(input("enter the number of elements"))
b=[]
for i in range(0,n2+1):
    c=int(input("Enter the element:"))
    b.append(c)
new=a+b
new.sort()
print(new)
