t = int(input())
count = 0
for _ in range(t):
    l = list(map(int,input().split()))
    for i in range(len(l)):
        if l[i] == 7:
            count+=1
    if count >= 1:
        print("YES")
    else:
        print("NO")


# the constraints need to be implemented