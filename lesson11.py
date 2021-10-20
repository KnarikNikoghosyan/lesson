# thedict = {"name": "Aram","year": 1994}
# print(thedict)

# x = thedict.popitem()
# print(x)

# thedict["year"] = 2014
# print(thedict)

# print(len(thedict))

# thedict["age"] = 26
# print(thedict)
# del thedict["year"]
# print(thedict)

# students = {"Aram": 19, "Sona": 15, "Ani": 18, "Robert": 11, "Syuzi": 16,
			# "David": 17, "Karine": 14, "Gurgen": 8, "Anna": 13, "Hasmik": 19}
# counts = 20
# for i in students:
# 	if students[i] > counts:
# 		counts = students[i]
# for i in students:
# 	if students[i] == counts:
# 		print(i,counts)


# for i in students:
# 	if students[i] < counts:
# 		counts = students[i]
# for i in students:
# 	if students[i] == counts:
# 		print(i,counts)
# counts = 0
# for i in students:
# 	counts += students[i]
# print(counts / len(students))

# for i in students:
# 	if students[i] >= 5:
# 		print(i, students[i])

# student = input("enter student's name ")
# if student in students:
# 	print("okay")
# else:
# 	print("no")

# s = 'a,2,b,5,c,8,a,4,e,11'.split(",")
# print(s)
# d = {}
# for i in range(0, len(s), 2):
# 	if s[i] in d:
# 		d[s[i]] += int(s[i+1])
# 	else:
# 		d[s[i]] = int(s[i+1])
# print(d)

# word = "exercises"
# thisdict = {}
# for i in word:
# 	thisdict[i] = word.count(i)
# print(thisdict)