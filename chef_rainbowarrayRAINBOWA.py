"""t  = int(input())
for i in range(t):
    n = int(input())
    d = list(map(int,input().split()))
    x = len(d)
    if len(d) == n-1:
        for z in range(0,len(d)):
            word = d[z]
            nword = d[x-z]
        if word == nword:
            print("yes")
        else:
            print("no")
    else:
        break"""

t = int(input())
i = 0
l = 0
a = []
for i in range(t):
    n = int(input())
    i+=1
    for l in range(n):
        d = list(map(int,input().split()))
        a.append(d)
        l+=1
        x = len(a)-1
for z in range(0,len(a)):
    for m in z:
            p = len(z)-1
            word == z[m]
            nword == z[p-m]
if word == nword:
    print("true")
else:
    print("no")
