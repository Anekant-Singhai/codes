for _ in range(int(input())):
    x, y = [int(a) for a in input().split()];
    if x%2 == 0:
        if (x+(2*y))%2 ==0:
            print("YES");
        else:
            print("NO");
    else:
        print("NO");