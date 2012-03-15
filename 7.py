# map(...)
    # map(function, sequence[, sequence, ...]) -> list
    
    # Return a list of the results of applying the function to the items of
    # the argument sequence(s).  If more than one sequence is given, the
    # function is called with an argument list consisting of the corresponding
    # item of each sequence, substituting None for missing values when not all
    # sequences have the same length.  If the function is None, return a list of
    # the items of the sequence (or a list of tuples if more than one sequence).

#Example1
print map(ord, 'asd')
# [97, 115, 100]

#Example2
print map(lambda x:x**2, [1, 2, 3])
# [1, 4, 9]

#Example3
#Do see the use of two lists to fulfill two arguments of the lambda function.
print map(lambda x, y: x*y**2, [1, 2, 3], [2, 4, 1])
# [4, 32, 3]