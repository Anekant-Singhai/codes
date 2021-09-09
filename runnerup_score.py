n = int(input())
v = list(map(int,input().split()))
v = sorted(v)
max = max(v[0],v[1])
secondmax = min(v[0],v[1])
if len(v) == n:

    for i in range(2,len(v)):
        if v[i]>max:
            secondmax = max
            max = v[i]
        elif v[i]>secondmax and v[i]!=max:
            secondmax = v[i]
    print(secondmax)


else:
    print("error")
