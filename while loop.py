#!/usr/bin/env python3

# while loop

'''syntax for while loop
while condition:
		body            '''


a,b =0,1
print(a,b)

while a < 100:
	print(a)
	a,b=b,a+b
	#a,b=b,a+b
	

i=1
n=5

while i<= n:
	print(i)
	i=i+1
	
	
	
	#Another example
i=2
while i<100:
	i=i**2
	print(i)
	
	#Program to calculate the sum of numbers until the user enter zero
	
total = 0
number= int(input('Enter a number = '))
#add number until zero
while number != 0:
	total += number #total = total + number;
	
	# take integer input again
	number = int(input('Enter a number = '))
	
print('Total = ', total)


#Exercise write a code to get sum of all numbers less than any input number
