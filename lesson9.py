# tup1 = ('physics', 'chemistry', 1997, 2000)
# print(tup1.__sizeof__())


# fruits = ("apple", "mango", "banana", "cherry")
# for i in fruits:
#     if i == "banana":
#         continue
#     print(i)


# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))
# my_tuple = tuple(range(100))
# print(my_tuple)

# thistuple = ("apple", "banana", "cherry")
# print(thistuple.count("banana"))

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#  print("Yes 'apple' is in the fruits tuple")

# thistuple = ("apple", "banana", "cherry","kiwi")
# print(thistuple[1])
# print(thistuple[0])
# print(thistuple[1:3])

# x = (5, 10, 15, 20)
# y = reversed(x)
# print(tuple(y))

# x = (1, 2, 3, 4, 5)
# # print(x[::-1])
# print(x[0:4:2])
# print(x[1:4:2])

# tuple1 = ("a", "b", "c")
# tuple2 = (1, 2, 3)
# tuple3 = tuple1 + tuple2
# print(tuple3)

# num = (10,20,30,(10,20),40)
# c = 0
# for n in num:
#     if isinstance(n, tuple):
#         break
#     c += 1
# print(c)

# tup = (1, 2, 3, True, False)
# c = 0
# for n in tup:
#     if isinstance(n, bool):
#         break
#     c += 1
# print(c)


# tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
# mystr = ''.join(tup)
# print(mystr)

# tup = ("Ann", "Ben", "David", "Arno", "Knarik")
# for i in range(len(tup) - 1):
#     print(tup[i],tup[i + 1])

# tup = (1, 2, 3, 4, 5)
# print(sum(tup))
# count = 0
# for i in tup:
#     count += i
# print(count)

# length = 0
# for i in tup:
#     length += 1
# print(length)

# print(sum(tup) / len(tup))

tup2 = (2, 6, 7, 1, 5)
# print(sorted(tup2))
# print(max(tup2))
# print(min(tup2))
start = tup2[0]
# for i in tup2:
#     if i > start:
#         start = i
# print(start)

# for i in tup2:
#     if i < start:
#         start = i
# print(start)

# result = 1
# for i in tup2:
#     result *= i
# print(result)

# c = tuple(sorted(tup2))
# print(c[-2:])
# print(c[0])
# print(c[-1])

# print(tup2.index(6))
