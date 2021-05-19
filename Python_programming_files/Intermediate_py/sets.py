#SETS : unordered , mutable , no duplicates

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)

#myset.discard(3)#better because it doesnt show any error if the element doesnt exist
#myset.remove can leadto errors or exceptions
#myset.pop() arbitrarily will remove an element and remove it from the set

sum=0

if 1 in myset:
    print("True")

for i in myset:
    sum += i
print(sum)
print(myset)


odds = {1,3,5,7,9}
evens = {0,2,4,6,8,10}
primes = {2,3,5,7,11,13}

u = odds.union(evens)
print(u)

intr = odds.intersection(primes)
print(intr)

temp = u.difference(intr)
print(temp)
