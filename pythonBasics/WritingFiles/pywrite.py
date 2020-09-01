#Writing into files and creating files with python


append_toFile = open("pythonBasics/WritingFiles/filer.txt","a")

# when you set the mode of the file to append it adds to the end of the file 
# NOTE: if you do not add next line at the end of what 
# you want to write it appedns to the end of the file
new_employee = str(input("name of employee 1\n"))
new_employee2 = str(input("name of employee 2\n"))
print(append_toFile.write(f"{new_employee} \n"))
print(append_toFile.write(f"{new_employee2} \n"))


liter = [1,2,3,4,5]

for index in range(len(liter)+1):
    namer = input(f"Employee {index} : \n")
    print(append_toFile.write(f"{namer} \n"))

append_toFile.close()