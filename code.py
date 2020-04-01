#0 2 2 4 -> 0 3 4 2

a = []
a = list(map(int,input().rstrip().split()))
y = len(a)
x1 = a[0]
v1 = a[1]
x2 = a[2]
v2 = a[3]

t1 = x1 - x2 
t2 = v2 - v1 



if(t2 == 0 or t1 % t2 != 0 or t1 / t2 < 0):
    print('NO')

else:
    print('YES')

