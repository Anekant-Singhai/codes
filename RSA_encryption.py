import itertools

def gcd(x,y):
    while(y):
        x,y = y,x%y
    return x



print("p and q:")
p,q = int(input().split())
for i,j in itertools.product(range(p),range(q)):
    if gcd(i,p) != 1:
        print("p isn't a prime")
    elif (gcd(j,q) != 1):
        print("q isn't a prime")

# finding the euler totient
count=0
n = p*q
print(" the n is: ",n)
for k in range(n):

    if gcd(k,n) == 1:
        count+=1
print(" the phi is: ",count)
#finding e
e = 2
while (e < count):
    if (gcd(e,count) == 1):
        break;
    else:
        e++
print("the e is: ")
print("the msg sir?: ")
msg = input()



