toDoList = []


def printlist():
    counter = 1
    for x in toDoList:
        if x[1] == False:
            print(counter, ".", x[0], ": [ ]")
        else:
            print(counter, ".", x[0], ": [X]")
        counter += 1

def createToDo():
    newToDo = input("What do you need to do today?\n")
    toDoList.append((newToDo, False))

def updateToDo():
    updateItem = int(input("Which item do you want to toggle?")) - 1
    print(toDoList[updateItem])
    # toDoList[updateToDo] = not toDoList[updateToDo]


while True:
    printlist()
    # print(toDoList)
    choice = input("What would you like to do? 1. Create a To Do Item | 2. Toggle To Do Item | 3. Cancel\n")
    if choice == "1":
        createToDo()
    elif choice == "2":
        updateToDo()
