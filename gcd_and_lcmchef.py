def gcd(s,r):
    while (r):
        s,r = r,s%r
    return s

def lcm(p,q):
    if p > q:
        big = p
    else:
        big = q
    while(True):
        if((big%p == 0) and (big%q == 0)):
            lcm = big
            break
        big+=1
    return lcm

print(lcm(16,36))
for _ in range(int(input())):
    x,y = [int(l) for l in input().split()]
    print(gcd(x,y),lcm(x,y))
