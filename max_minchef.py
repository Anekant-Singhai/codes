for _ in range(int(input())):
    n = int(input())
    s = 0
    a = list(map(int, input().split()))
    if len(a) == n:
        for i in range(len(a)-1): # via this we can access the two elements consecutive each time, we used list slicing
            y = max(a[i:i+2])
            print("y is ", y)
            x = min(a[i:i+2])
            print("x is " ,x)
            s = s+x
            print("the s is ", s)
            a.remove(y)
            print(a)
        print(s)
