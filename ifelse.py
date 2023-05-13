#!/usr/bin/env python3

#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

#Example 1

#a = 33
#b = 200
#if b > a:
#	print("b is greater than a")
#	
#	
##Example 2
#	
#	
#a1 = 33
#b1 = 200
##if b1 > a1:
##print("b1 is greater than a1") # you will get an error
#
#
##Example 3
#
#
#a = 33
#b = 33
#if b > a:
#	print("b is greater than a")
#elif a == b:
#	print("a and b are equal")
#
#	
#a = 200
#b = 33
#if b > a:
#	print("b is greater than a")
#elif a == b:
#	print("a and b are equal")
#else:
#	print("a is greater than b")
#	
#	
##short hand 
#	
#	
#a = 2
#b = 330
#print("A") if a > b else print("B")
#

##short hand 2
#a = 330
#b = 330
#print("A") if a > b else print("=") if a == b else print("B")





##use of two conditions  with 'and'
#
#a = 200
#b = 33
#c = 500
#if a > b and c > a:
#	print("Both conditions are True")
#
#	
#	
##Example
#
##use of two conditions  with 'or'
#	
#a = 200
#b = 33
#c = 500
#if a > b or a > c:
#	print("At least one of the conditions is True")
#	
##use of two conditions  with 'not'	
#a = 33
#b = 200
#if not a > b:
#	print("a is NOT greater than b")	
#	
##Example	
#x = 41
#
#if x > 10:
#	print("Above ten,")
#	if x > 20:
#		print("and also above 20!")
#	else:
#		print("but not above 20.")
#		
#		
## if you want to leave the if statement empty
#a = 33
#b = 200
#
#if b > a:
#	pass