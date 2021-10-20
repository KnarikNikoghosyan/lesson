# my_list = 'Hello world'
# my_list = my_list.split()
# my_list = my_list.split(',')
# print(my_list)


# fruits = ["banana" , "apple" , "cherry"]
# fruits[1] = "kiwi"
# print(fruits)

# fruits = ["banana" , "apple" , "cherry"]
# fruits.append("orange")
# print(fruits)

# fruits = ["banana" , "apple" , "cherry"]
# fruits.insert(1 , "orange")
# print(fruits)

# fruits = ["banana" , "apple" , "cherry"]
# fruits.remove( "apple")
# print(fruits)

# fruits = ["banana" , "apple" , "cherry"]
# x = fruits.pop()
# print(fruits,x)

# fruits = ["banana" , "apple" , "cherry"]
# del fruits[2]
# # del fruits
# print(fruits)

# fruits = ["banana" , "apple" , "cherry"]
# numbers = [34, 56 , -456, 7.56, - 2.34]
# fruits.extend(numbers)
# print(fruits)

# numbers= [34, 56 , -456, 7.56, - 2.34]
# numbers.sort()
# print(numbers)

# numbers = [34, 56 , -456, 7.56, - 2.34]
# numbers.reverse()
# print(numbers)

# list1 = [1, 'Text', (5.6 , 7.7)]
# list2 = [1, 'Text', (5.6 , 7.7)]
# print(list1 == list2)
# print(list1 is list2)

# my_list = [ i for i in range(10)]
# print(my_list)

# my_list = []
# for i in range(10):
#     my_list.append(i)
# print(my_list)

# my_list = [ i ** 2 for i in range(100) if i % 2 == 0 ] 
# print(my_list)

# my_list = []
# for i in range(100):
#     if i % 2 == 0:
#         my_list.append(i**2)
# print(my_list)

# my_list = [1, 3, 4, 5, 1, 2, 3, 1]
# x = 0
# for i in my_list:
#     if my_list.count(i) > x:
#         x = my_list.count(i)
# print(x)

# for i in my_list:
#     if my_list.count(i) == x:
#         print(i)
#         break

# list1 = [25, True, "abc", (1,2), [5,6], 5.3, range(10)]

# my_list = ["Hp", "Asus", "Dell", "Mac", "Lenovo"]
# if "Hp" in my_list:
#     print("okay")


# while True:
#     numbers = 0
#     chars = 0
#     password = input("enter a password ")
#     if not len(password) > 8:
#         print("your password length is ", len(password), "it must be more than 8")
#         continue
#     if not(password[0].isupper() and password[0].isalpha()):
#         print("your first letter must be upper but your first letter is", password[0])
#         continue
#     for i in password:
#         if i.isdigit():
#             numbers += 1
#         elif i in ("*", "/", "#", "+", "=", "~"):
#             chars += 1
#     if numbers < 2:
#         print(f"you must have more than {numbers} you should have 2 or more numbers")
#         continue
#     if chars < 2:
#         print(f"you must have more than {chars} you shold have 2 or more chars") 
#         continue
#     print("your password is strong", password)
#     break


# link = "https://www.youtube.com/watch?v=RRW2aUSw5vU"
# count = 0
# for i in link:
#     if i == "=":
#         break
#     count += 1
# print(count)
# print(link[count +1:])

# print(link[link.index("=") + 1:])

# word = input("enter a word ")
# if word == word[::-1]:
#     print("okay")
# else:
#     print("no")