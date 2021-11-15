# we need to define the limits for l[i] but how do we do that? any ideas?
t = int(input())
draw = 0;bharat = 0;eng = 0;
for _ in range(t):
    l = list(map(int,input().split()))
    for i in range(len(l)):
        if l[i] == 0:
            draw +=1
        elif l[i] == 1:
            bharat +=1
        elif l[i] == 2:
            eng +=1
    if bharat > eng:
        print("INDIA")
    elif bharat < eng:
        print("ENGLAND")
    elif bharat == eng:
        print("DRAW")
    
        