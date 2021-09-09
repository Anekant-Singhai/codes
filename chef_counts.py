t = int(input())
count = 0

for count in range(t):
    x,y = [int(j) for j in input().split()]
    count+=1
    l=[max(x,y),x+y]
    
    print(*l)
