import json
import random
from verify import verify

def createTask(name, weight):
    taskDataEntry = {"taskName": name,
                     "weight": weight}
    with open('tasks.json', encoding = 'utf-8') as tasks:
        taskData = json.load(tasks)
        if len(taskData) == 0:
            if name != "cancel" or weight != "cancel":
                taskData.append(taskDataEntry)
                file = open('tasks.json', 'w')
                json.dump(taskData, file, indent = 2)
                file.close()
        else:
            filtered = [task["taskName"] for task in taskData]
            if name in filtered:
                print(f"{name} has already been found within the json!")
            else:
                if name != "cancel" or weight != "cancel":
                    taskData.append(taskDataEntry)
                    file = open('tasks.json', 'w')
                    json.dump(taskData, file, indent = 2)
                    file.close()

def updateWeight(name, newWeight, index):
    taskDataEntry = {"taskName": name,
                     "weight": newWeight}
    with open('tasks.json', encoding = 'utf-8') as tasks:
        taskData = json.load(tasks)
        taskData[index] = taskDataEntry
        file = open('tasks.json', 'w')
        json.dump(taskData, file, indent = 2)
        file.close()

def randomTask():
    with open('tasks.json', "r", encoding = "utf-8") as tasks:
        taskData = json.load(tasks)
        randomList = []
        for task in taskData:
            i = 0
            while i < int(task["weight"]):
                randomList.append(task["taskName"])
                i += 1
        randTask = int(random.randint(1, len(randomList)))
        print("""
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄⠄⠄⠄⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⢀⣀⣀⣀⡀⠄⢀⣠⡔⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣰⢿⣿⣿⣿⣿⣿⣿⣷⡆⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣻⣟⣿⣿⡿⣟⣛⣿⡃⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣾⣿⣷⣿⣷⣿⣿⣿⣷⣽⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⡟⣟⣿⣿⠺⣟⣻⣿⣿⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡝⠻⠵⠿⠿⢿⣿⣿⢳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣧⠈⣛⣛⣿⣿⡿⣡⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠄⠙⠛⠛⢁⣴⣿⣿⣷⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⡿⠟⠉⠄⠄⢠⠄⣀⣠⣾⣿⣿⡿⠟⠁⠄⠈⠛⢿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⡟⠉⠄⠄⢀⠠⠐⠒⠐⠾⠿⢟⠋⠁⠄⢀⣀⠠⠐⠄⠂⠈⠻⢿⣿⣿
        ⣿⣿⣿⠋⠁⠄⢀⡈⠄⠄⠄⠄⠄⠄⠄⠄⠁⠒⠉⠄⢠⣶⠄⠄⠄⠄⠄⠈⠫⢿
        ⣿⣿⡟⠄⢔⠆⡀⠄⠈⢀⠄⠄⠄⠄⠄⠄⠄⢄⡀⠄⠈⡐⢠⠒⠄⠄⠄⠄⢀⣂
        ⣿⣿⠁⡀⠄⠄⢇⠄⠄⢈⠆⠄⠄⢀⠔⠉⠁⠉⠉⠣⣖⠉⡂⡔⠂⠄⢀⠔⠁⠄
        ⣿⡿⠄⠄⠄⠄⢰⠹⣗⣺⠤⠄⠰⡎⠄⠄⠄⠄⠄⠄⠘⢯⡶⢟⡠⠰⠄⠄⠄⠄
        """)
        print(f"You should {randomList[randTask-1]}. NOW!")

def searchSingleTask(data):
    with open('tasks.json') as tasks:
        taskData = json.load(tasks)
        filtered = [task["taskName"] for task in taskData]
        if data in filtered:
            print(f"The task, {data}, has been found.")
            print("Would you like to:\n[A] Change the weight\n[B] Delete the tag\n[C] Return to the main menu\n")
            choice = verify(3)

            if choice == 'a':
                #change weight
                newWeight = input("What would you like to change the weight to?")
                updateWeight(data, newWeight, filtered.index(data))
            elif choice == 'b':
                removeTask(data)
        else:
            print('Task not found!')

def searchAllTask():
    with open('tasks.json') as tasks:
        taskData = json.load(tasks)
        for task in taskData:
            print(task)

def removeTask(data):
    if data != "cancel":
        with open('tasks.json', 'r', encoding = 'utf-8') as tasks:
            taskData = json.load(tasks)
            filtered = [task["taskName"] for task in taskData]
            if data in filtered:
                print(f"{data} has been successfully removed")
                taskData.pop(filtered.index(data))
            else:
                print('Task not found!')

        with open("tasks.json", 'w', encoding = 'utf-8') as f:
            f.write(json.dumps(taskData, indent = 2))

def removeAllTasks():
    with open("tasks.json", 'w', encoding = 'utf-8') as f:
            f.write("[]")