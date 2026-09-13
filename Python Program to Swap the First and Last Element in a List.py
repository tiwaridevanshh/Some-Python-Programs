n=int(input("Enter the number to be inserted in list"))
a=[]
for i in range(0,n):
    b=int(input("Ennter the numbe"))
    a.append(b)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print("the new list is ")
print(a)
