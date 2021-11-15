for _ in range(int(input())):
    s1 = input()
    s2 = input()
    a = []
    b = []
    c = []
    for i in range(len(s1)):
        a.append(s1[i])
    for j in range(len(s2)):
        b.append(s2[j])
    for j in range(len(s2)):
        n = s1.index(s2[j])
        c.append(n+1)
        d = [x-c[k-1] for k, x in enumerate(c)][1:]
        d = [abs(num) for num in d]
    print(sum(d))
