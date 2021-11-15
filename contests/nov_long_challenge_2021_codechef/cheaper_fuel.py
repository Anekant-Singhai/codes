for _ in range(int(input())):
    a = list(map(float, input().split()))
    a[3] = a[3]*a[4]
    a[2] = a[2]*a[4]
    a[1] = a[1]+a[3]
    a[0] = a[0]+a[2]

    if a[0] > a[1]:
        print("DIESEL")
    elif a[1] > a[0]:
        print("PETROL")
    elif a[1] == a[0]:
        print("SAME PRICE")
