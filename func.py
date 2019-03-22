def choice(answer):
	if answer > 5:
		print("overaged")
	elif answer <=5:
		print("welcome to the club")
	else:
		print("young")

print(choice(6))
print(choice(2))
print(choice(10))