"""import re
t = int(input())
x = [input() for l in range(t)]

for i in x:
    q = re.findall("4", i)
    if q:
        print(len(q))
    else:
        print(0)"""


w = [44,4444,32,432]
for i in range(0,len(w)):
    print(w[i]+1)
    print(w.index(w[i]))
