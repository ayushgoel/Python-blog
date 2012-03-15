#Using try-except block

def dic(words):
	a = {}
	for i in words:
		try:
			a[i] += 1
		except KeyError:   ## the famous pythonic way:
			a[i] = 1       ## Halt and catch fire
	return a

# >>> a='1,3,2,4,5,3,2,1,4,3,2'.split(',')
# >>> a
# ['1', '3', '2', '4', '5', '3', '2', '1', '4', '3', '2']
# >>> dic(a)
# {'1': 2, '3': 3, '2': 3, '5': 1, '4': 2}


#Without using try-catch block

def dic(words):
	data = {}
	for i in words:
		data[i] = data.get(i, 0) + 1
	return data

# >>> a
# ['1', '3', '2', '4', '5', '3', '2', '1', '4', '3', '2']
# >>> dic(a)
# {'1': 2, '3': 3, '2': 3, '5': 1, '4': 2}
