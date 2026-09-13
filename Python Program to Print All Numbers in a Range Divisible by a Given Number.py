lower = int(input("Enter the lower range"))
upper = int(input("enter the upper range"))
n = int(input("enter the number to be divided"))
for i in range(lower,upper+1):
    if i%n==0:
        print(i)
