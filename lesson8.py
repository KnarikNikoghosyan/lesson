import random


print("Hi guys,you play the game 21 ")
name = input("What's your name? ")
start = random.choice("pu")
point = 0
end = 3
if start == "p":
	print("start comp")
	while True:
		if point > 18:
			end = 21 - point
		if point % 4 == 0:

			comp = random.randint(1, end)
		else:
			comp = 4 - point % 4
		print(f"{point} + {comp} = {point + comp}")
		point += comp
		if point == 21:
			print("win user")
			break
		if point > 18:
			end = 21 - point

		while True:
			user = input(f"please write number between 1-{end} ")
			if user.isdigit():
				user = int(user)
				if user > 0 and user < end + 1:
					print(f"{point} + {user} = {point + user}")
					point += user
					break
				else:
					print(f"please 1-{end}")
			else:
				print("please write number")

		if point == 21:
			print("win pc")
			break



else:
	print("start user")
	while True:

		while True:
			if point > 18:
				end = 21 - point
			user = input(f"please write number between 1-{end} ")
			if user.isdigit():
				user = int(user)
				if user > 0 and user < end + 1:
					print(f"{point} + {user} = {point + user}")
					point += user
					break
				else:
					print(f"please 1-{end}")
			else:
				print("please write number")

		if point == 21:
			print("win pc")
			break
		comp = 4 - point % 4
		print(f"{point} + {comp} = {point + comp}")
		point += comp


