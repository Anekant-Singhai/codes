a = 0
b = 1
n = int(input("the terms are: "))
count = 0
sum = 0
u = []
while count<=n:

      a=b
      b=sum
      sum = a+b           

      count+=1
      u.append(sum)
print(u)
