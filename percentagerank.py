



students = {}
for _ in range(int(input())):
    name,*marks = input().split()
    scores = list(map(float,marks))
    students[name] = scores
n = input()
for k,v in students.items():
    for i in range(0,len(v)):
        y = sum(v)/len(v)

    if  k == n:
        print('{0:.2f}'.format(y))
