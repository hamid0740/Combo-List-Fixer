class color:
	purple = '\033[35m'
	red = '\033[31m'
	yellow = '\033[33m'
	green = '\033[92m'
	blue = '\033[36m'
	reset = '\033[0m'

print(color.purple + "App name: " + color.reset + "Combo Fixer")
print(color.purple + "Version: " + color.reset + "1.1")
print(color.purple + "Developer: " + color.reset + "hamid0740")
print(color.purple + "GitHub: " + color.reset + "https://github.com/hamid0740/Combo-Fixer" + "\n")

print(color.blue + "Make sure that this Python code is in the same directory with the combo you want to fix.")
file_name = input(color.yellow + "Enter your file name: " + color.reset)
separator = input(color.yellow + "Enter your desired separator: " + color.reset + "\n")

file = open(file_name, "r")
line_count = 0
for line in file:
	if line != "\n":
		line_count += 1
file.close()

with open(file_name, 'r') as file:
	data = file.readlines()

i = 1
for i in range(line_count):
	head, sep, tail = data[i].partition(separator)
	if i+1 != line_count:
		data[i] = head + "\n"
	else:
		data[i] = head

with open(file_name, 'w') as file:
	file.writelines(data)
	
print(color.green + "Successfully edited " + str(line_count) + " lines in the " + file_name + " file." + color.reset)
