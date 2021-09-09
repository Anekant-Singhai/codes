def siddh(n):
    if n==0:
        return 1
    else:
        return(n*siddh(n-1))

t = int(input())
u = []
for x in range(0,t):
    i = int(input())
    l = siddh(i)
    u.append(l)
    x+=1

for r in range(0,len(u)):
    print(u[r])
"""i tested it upto 900"""
