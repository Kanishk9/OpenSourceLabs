str1 = "Hello World"
frequency = {}
for i in str1:
	if i in frequency:
		frequency[i] += 1
	else:
		frequency[i] = 1

print (frequency)