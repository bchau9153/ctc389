#Benson Chau
#Lab 6

studentlist = ["Kayla", "Elsy", "Ximena", "Bryna", "Nena"]
for i in studentlist:
    print(i)
selection = float(input("You are allowed to make changes to the list with these options:\n 1: Add student to list\n 2: Modify student name\n 3: Remove student\n Select an option by inputting the corresponding number: "))
if selection == 1:
    newname = input("What is the student's name? ")
    studentlist.append(newname)
    for j in studentlist:
        print(j)
elif selection == 2:
    counter = 0
    for q in studentlist:
        counter = counter + 1
        print(q, counter)
    nameselect = int(input("Enter the numbered position that you want to modify the name for: ")) - 1
    modname = input("What is the new name? ")
    studentlist[nameselect] = modname
    for k in studentlist:
        print(k)
elif selection == 3:
    counter = 0
    for w in studentlist:
        counter = counter + 1
        print(w, counter)
    nameselect = int(input("Enter the numbered position of the name you want to remove: ")) - 1
    studentlist.pop(nameselect)
    for l in studentlist:
        print(l)

