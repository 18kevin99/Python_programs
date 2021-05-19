example = ['left' , 'right' , 'up' , 'down']
#instead of doing
##for i in range(len(example)):
##      print(i, example[i])

#do

for i,j in enumerate(example):
    print(i,j)

#list to dict
new_dict = dict(enumerate(example))
print(new_dict)

x = [1,2,3,4]
y = [5,6,7,8]
z = ['a','b','c','d']

# you could do this
##for a,b,c in zip(x,y,z):
##    print(a,b,c)

# but better u do this
[print(a,b,c) for a,b,c in zip(x,y,z)]

#NOTE
#this prints the tuples
for i in zip(x,y,z):
    print(i)
#this is a list of tuples
print(list(zip(x,y,z)))
#dict with x as index
print(dict(zip(x,y)))
