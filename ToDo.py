class ToDoItem:
    def __init__(self, text):
        self.text = text
        self.isDone = False

    def __str__(self):
        return self.text

toDoList = []


def printList():
    counter = 1
    for x in toDoList:
        if x.isDone is False:
            print(counter, ".", x.text, ": [ ]")
        else:
            print(counter, ".", x.text, ": [X]")
        counter += 1

def createToDo():
    newText = input("What do you need to do today?\n")
    newItem = ToDoItem(newText)
    toDoList.append(newItem)

def updateToDo():
    updateItem = int(input("Which item do you want to toggle?\n")) - 1
    toDoList[updateItem].isDone = not toDoList[updateItem].isDone


while True:
    printList()
    choice = input("What would you like to do? 1. Create a To Do Item | 2. Toggle To Do Item | 3. Cancel\n")
    if choice == "1":
        createToDo()
    elif choice == "2":
        updateToDo()
    elif choice == "3":
        exit()
