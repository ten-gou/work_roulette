import os
import string
from task_functions import createTask, checkEmpty, randomTask, searchSingleTask, searchAllTask, removeTask, removeAllTasks
from verify import verify

def work_roulette():
    if os.path.isfile('tasks.json') == False:
        open("tasks.json", "x")

    empty = checkEmpty()

    print('What would you like to do?')
    print('[A] Add a new task') #CreateTask
    print('[B] Choose a random task') #RandomTask
    print('[C] See the full task list') #SearchAllTask
    print('[D] Check for an individual task') #SearchSingleTask
    print('[E] Delete a task') #RemoveTask
    print('[F] Delete all tasks') #RemoveAllTasks
    print('[G] End function')
    action = verify(7)

    if action == 'a':
        name = input("Input the new task that you would like to add to the list:")
        weight = input("Input the weight/importance of the task:")
        while weight not in string.digits or len(weight) < 1:
            weight = input("Please input a number")
        createTask(name, weight)
    elif action == 'b' and empty == False:
        randomTask()
    elif action == 'c' and empty == False:
        searchAllTask()
    elif action == 'd' and empty == False:
        taskSelect = input("Which task are you searching for?").casefold()
        searchSingleTask(taskSelect)
    elif action == 'e' and empty == False:
        taskSelect = input("Which task do you want to remove?").casefold()
        removeTask(taskSelect)
    elif action == 'f':
        removeAllTasks()
    elif action == 'g':
        print('Goodbye!')
        exit()
    work_roulette()

work_roulette()