t = int(input())
for _ in range(t):
    s = input()
    s1 = s[0]+s[1]
    s1 = s1*int(len(s)/2)
    if len(s)%2:
        s1 += s[0]
        #ababa
    if s == s1:
        print("YES")
    else:
        print("NO")
