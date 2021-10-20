import time
import random


# while True:
# 	print("Hello")
# 	break


# salary = 0
# while salary < 500:
# 	telcell = int(input("money "))
# 	salary += telcell
# print(salary)


# i = 1
# while i < 6:
#  	if i == 3:
#  		break
#  	i += 1
#  	print(i)

# while True:
#  localtime = time.localtime()
#  result = time.strftime("%I:%M:%S %p", localtime)
#  print(result)
#  time.sleep(1)


# number1 = int(input("number "))
# number2 = int(input("number "))
# if number1 > number2:
# 	maximum = number1
# 	minimum = number2
# elif number2 > number1:
# 	maximum = number2
# 	minimum = number1
# elif number1 == number2:
# 	minimum = maximum = number1

# for i in range(2, minimum):
# 	if number1 % i == 0 and number2 % i == 0:
# 		print(i)
# 		break
# else:
# 	print(1)


# even = 0
# odd = 0
# for i in range(1, 100):
# 	if i % 2 == 0:
# 		even += 1
# 	else:
# 		odd += 1
# print(even, odd)

# x,y = 0,1
# while x < 40:
# 	print(x)
# 	x,y = y,x+y

# number = 0
# letter = 0
# string = "abc 123"
# for i in string:
# 	if i.isdigit():
# 		number += 1
# 	elif i.isalpha():
# 		letter += 1
# print(number, letter)

# count = 0
# number = int(input("enter a number "))
# for i in str(number):
# 	count += int(i)
# print(count)

# result = 1
# number = int(input("enter a number "))
# for i in range(1, number+1):
# 	result *= i
# print(result)

# result = 0
# text = "abcd"
# for i in text:
# 	result += 1
# print(result)


# number1 = int(input("enter a number "))
# number2 = int(input("enter a number "))
# if number1 > number2:
# 	maximum = number1
# 	minimum = number2
# elif number2 > number1:
# 	maximum = number2
# 	minimum = number1
# elif number1 == number2:
# 	minimum = maximum = number1
# for i in range(minimum, 0, -1):
# 	if number1 % i == 0 and number2 % i == 0:
# 		print(i)
# 		break

# counter = 0
# number1 = int(input("enter a number "))
# number2 = int(input("enter a number "))
# if number1 > number2:
# 	maximum = number1
# 	minimum = number2
# elif number2 > number1:
# 	maximum = number2
# 	minimum = number1
# elif number1 == number2:
# 	minimum = maximum = number1
# for i in range(maximum, number1*number2 + 1, maximum):
# 	counter += 1
# 	if i % number1 == 0 and i % number2 == 0:
# 		print(i)
# 		break
# print(counter)


# string = "abcd"
# while True:
# 	text = input("letter ")
# 	if text in string:
# 		print("okay")
# 		break
# 	else:
# 		print("wrong")



# count_user = 0
# count_pc = 0
# while True:
# 	number1 = random.randint(1, 6)
# 	number2 = random.randint(1, 6)
# 	print("user", number1, "pc", number2)
# 	if number1 > number2:
# 		count_user += 1
# 	elif number2 > number1:
# 		count_pc += 1
# 	elif number1 == number2:
# 		print("=")
# 	if count_pc == 2:
# 		print("win pc")
# 		break
# 	elif count_user == 2:
# 		print("win user")
# 		break

