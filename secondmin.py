v = [7,2,3,5,1]
v = sorted(v)
min = min(v[0],v[1])
secondmin = max(v[0],v[1])
for i in range(2,len(v)):
    if v[i] < min:
        secondmin = min
        min = v[i]
    elif secondmin > v[i] and min!=v[i]:
        secondmin = v[i]
print(secondmin)
