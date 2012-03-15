# Initial Code

def append_s(words):
	new_words=[]
	for word in words:
		new_words.append(word + 's')
	return new_words

for word in append_s(['a','b','c']):
	print word

	
# Better Version

def append_s(words):
	return [i+'s' for i in words] ## another list comprehension :D

for word in append_s(['a','b','c']):
	print word