n,k = [int(l) for l in input().split()]
t = [int(input()) for w in range(0,n)]
counter = 0
for i in t:
    if(i%k == 0):
        counter +=1
print(counter)


n,k = [int(l) for l in input().split()]
i=0
counter = 0
for i in range(0,n):
    temp = int(input())
    i+=1
    if(temp%k == 0):
        counter+=1
print(counter)        
