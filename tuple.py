'''
t=1,2,3,4
print(t)
t1=(10,3+4j,"String")
print(t1)

t=1,
print(type(t))
print(t)

t=()
print(t)

l=[1,2,3,4]
t=tuple(l)
print(t)

t=tuple(range(10,20,2))
print(t)
print(t[::2])

t=[1,2,3,44]
t[1]=33
print(t)

t=(1,2,3,44)
t[1]=33
print(t)

Mathematical Operators for tuple


t1=(1,2,3,4)
t2=(3,4,5)
t3=t1+t2
print(t3)

t5=3*t2
print(t5)

t5=1,2,3,4,5,3,3,3
print(t5.count(3))

t=[1,2,[3],4]
y=t[2]
y.append(20)

t5=1,2,3,4,5,3,3,3
print(max(t5))
a=2
b=4
c=7
v=5
g=a,b,c,v
print(g)
q,w,e,r=g
print(q)
print(w)
print(e)
print(r)

t=(x**2 for x in range(1,5))
print(t)
t = eval(input("Enter your tuple"))
print(t)
l=len(t)
sum1=0
for i in t:
    sum1=sum1+i
print(sum1)
print(sum1/l)

s='-5//3'
print(len(s))

s="bed and breakfast"
r = s.find("bed")== False
print(r)
'''
s ="smart"
print(s[:-100:-2])

l=[1,2,3,4]
t=tuple(l)
print(t)





































































