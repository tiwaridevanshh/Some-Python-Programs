print("Enter the three numbers to find the no. of patterns")
a = [int(x) for x in input().split()]
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j and j!=k and k!=i):
                print(a[i],a[j],a[k])
