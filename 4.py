# Example1
class abc():
	pass

# Example1
for i in xrange(100):
	if condition1:
		do_something1()
	
	## If condition2 is fulfilled, the control enters the loop.
	## Since it's just a pass condition, the 
	## control goes back to for loop after it.
	## In this case, continue would give the same behaviour.
	elif condition2:
		pass
	
	else:
		do_something2()