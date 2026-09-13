n = int(input("Enter the no. of elements to be inserted :"))
a=[]
for x in range(n):
    elem= int(input("enter the element to be inserted in list"))
    a.append(elem)
avg=sum(a)/n
print("The average of the elments is :",avg)
    
