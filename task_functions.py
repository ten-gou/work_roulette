import json
import random

def createTask(name, weight):
    taskDataEntry = {"taskName": name,
                     "weight": weight}
    with open('tasks.json', encoding = 'utf-8') as tasks:
        taskData = json.load(tasks)
        taskData.append(taskDataEntry)
        duplicate = False

        if len(taskData) == 0:
            file = open('tasks.json', 'w')
            json.dump(taskData, file, indent = 2)
            file.close()
        else:
            for task in taskData:
                if name == task:
                    print(f"{task['taskName']} has already been found within the json!")
                    duplicate = True
            if duplicate == False:
                if name != "cancel" or weight != "cancel":
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
        print(f"You should {randomList[randTask-1]}. NOW!")

def searchSingleTask(data):
    with open('tasks.json') as tasks:
        taskData = json.load(tasks)
        i = 0
        for task in taskData:
            if data == task['taskName']:
                print(f"The task, {task['taskName']}, has been found.")
            elif i == len(task):
                print('Task not found!')
                break
            i+=1

def searchAllTask():
    with open('tasks.json') as tasks:
        taskData = json.load(tasks)
        for task in taskData:
            print(task)

def removeTask(data):
    if data != "cancel":
        with open('tasks.json', 'r', encoding = 'utf-8') as tasks:
            taskData = json.load(tasks)
            i = 0
            for task in taskData:
                if data == task['taskName']:
                    print(f"{task['taskName']} has been successfully removed")
                    taskData.pop(i)
                elif i == len(task):
                    print('Task not found!')
                    break
                i+=1

        with open("tasks.json", 'w', encoding = 'utf-8') as f:
            f.write(json.dumps(taskData, indent = 2))