t = int(input())
n = 0
c = []
count = 0
for n in range(t):
    i = int(input())
    p = 0
    for p in range(0,i):
        d = int(input())
        c.append(d)
        p+=1
    n+=1
for j in c:
        if j%2!=0:
            count+=1

print(count)



"""
t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    for _ in range(n):
        a = int(input())
        if a not in l:
            l.append(a)
        else:
            l.remove(a)
    print(l[0])"""
"""kaise bc"""
