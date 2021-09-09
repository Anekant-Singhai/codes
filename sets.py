############### different ways to create a set 

s = set([1,2,3,4,5])
e = {'a','b','c','d'}
t = set(('h','i','j','k'))

############## adding items

s.add(6) 
s.update([7,8,9],e) # the basic difference btw the upgrade and the add cmmnd is that by using add we can append only one item whereas by using upgrade we can append more
#PS: we can also add another set in this by using the upgrade method
print(s)


########## removing items 

s.remove("a")  #there is also a ccmnd called "discard". Discard doesn't throw an error when we try to remove any element not in a sets
s.discard(32)
s.discard(e)
print(s)

############ intersection of sets

s4 = s.intersection(t)
s5 = s.intersection(e)
l = s.intersection(t,e)
print(s4)
print(s5)

############### difference of sets

s6 = s.difference(e)
print(s6)

################# union of sets

x = s.union(t)
print(x)
################ loop through sets

for i in s:
	print(i,end = " ") #end parameter prints in one line

############ All elements but not duplicates
a = {11,22,33,44}
b = {55,22,77,44}
k = a.symmetric_difference(b)
print(k)



