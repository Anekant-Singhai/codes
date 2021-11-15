t = int(input())
count = 0
for _ in range(t):
    s = input()
    a = s[:]
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            count+=1
            
