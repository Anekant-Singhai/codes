def siddh(l,m,n):
    for i in range(n):
        for j in range(n):
            if l[j] == i+1:
                m.append(j+1)
    return(m)
            
while True:
    t = int(input())
    if t > 0:
        l1 = list(map(int,input().split()))
        l2 = []
        k = len(l1)
        l3 = siddh(l1,l2,k)
        if l3 == l1:
            print("ambiguous")
        else:
            print("not ambiguous")
    else:
        break

