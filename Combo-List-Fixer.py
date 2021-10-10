#Color for texts
class color:
	purple = '\033[35m'
	red = '\033[31m'
	yellow = '\033[33m'
	green = '\033[92m'
	blue = '\033[36m'
	reset = '\033[0m'

#App info
print(color.purple + "App name: " + color.reset + "Combo List Fixer")
print(color.purple + "Version: " + color.reset + "1.3")
print(color.purple + "Developer: " + color.reset + "hamid0740")
print(color.purple + "GitHub: " + color.reset + "https://github.com/hamid0740/Combo-List-Fixer" + "\n")

#First inputs
print(color.blue + "Make sure that this Python code is in the same directory with the combo list you want to fix.")
file_name = input(color.yellow + "Enter your file name: " + color.reset)
separator = input(color.yellow + "Enter your desired separator: " + color.reset)
print("")

#Reading file and counting lines
with open(file_name, 'r') as file:
	data = file.readlines()
	line_count = len(data)

#Fixing lines by separating
line_fixed = 0
for i in range(line_count):
	head, sep, tail = data[i].partition(separator)
	if separator in data[i]:
		if i+1 != line_count:
			data[i] = head + "\n"
		else:
			data[i] = head
		line_fixed += 1

#Applying edits to file and printing the result
if line_fixed != 0:
	with open("output.txt", 'w') as file:
		file.writelines(data)
	print(color.green + "Successfully edited " + str(line_fixed) + " out of " + str(line_count) + " lines in the '" + file_name + "' file.\nFixed file has been saved as '" + color.red + "output.txt" + color.green + "'." + "\n")
else:
	print(color.red + "No line has been edited.\nTry changing the separator or note that your combo list may not have any problems." + "\n")

#Asking to remove duplicate lines
to_rem_dup = input(color.yellow + "Do you also want to remove duplicate combos? (y/n): " + color.reset).lower()

#Removing duplicate lines
if to_rem_dup.startswith("y"):
	temp_data = []
	for i in data:
		if i not in temp_data:
			temp_data.append(i)

#Applying edits to file and printing the result
	if len(temp_data) < len(data):
		with open("output.txt", 'w') as file:
			file.writelines(temp_data)
		dup_lines = len(data) - len(temp_data)
		print(color.green + "Successfully removed " + str(dup_lines) + " duplicate combos.\nFixed file has been saved as '" + color.red + "output.txt" + color.green + "'." + color.reset)
	else:
		print(color.red + "There were no duplicate combos found." + color.reset)
