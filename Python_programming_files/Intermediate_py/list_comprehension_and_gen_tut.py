import timeit

'''xyz =[i for i in range(5000000)]
print('done')
xyz = (i for i in range(5000000))
print(xyz)'''
input_list = [5,6,2,10,15,20,5,2,1,3]
def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in input_list if div_by_five(i))

##xyz = []
##for i in input_list:
##    if div_by_five(i):
##        xyz.append(i)

##for i in xyz:
##    print(i)

##[print(i) for i in xyz]

# printing the combination of two series
##[[print(i,ii) for ii in range(5)] for i in range(5)]

#generator for the combination of two series with a list of the coupled elements
##xyz = ([[i,ii] for ii in range(5)]for i in range(5))
##print(xyz)


print(timeit.timeit('''input_list = range(100)
def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = list(i for i in input_list if div_by_five(i))''',number=5000))
