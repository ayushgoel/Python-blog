#List Comprehensions

#Example1
print [i for i in range(100)]

#Example2
print [i**2 for i in range(100)]

#Example3
a = [ord(i) for i in 'asfghj']
print a

#Example4
print [(a[i]+23)*4 for i in range(len(a))]
