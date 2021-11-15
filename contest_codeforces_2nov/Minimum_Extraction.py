
for _ in range(int(input())):
    a = list(map(int, input().split()))  # the minimum element
    while len(a) != 1:
        mini = min(a)
        for i in range(len(a)):
            a[i] = a[i]-mini
        a.remove(0)

    print(a)


#-1 2 0
#3 1
#2
