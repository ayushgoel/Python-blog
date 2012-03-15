def print_list(lst):
	
	for index, value in enumerate(lst):
		print "{0} -> {1}".format(index, value)
	
ls = [2, 5, 1, 6, 3]
print_list(ls)