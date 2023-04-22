import os
from task_functions import createTask, randomTask, searchSingleTask, searchAllTask, removeTask, removeAllTasks
from verify import verify

def work_roulette():
    if os.path.isfile('./tasks.json') == False:
        open("tasks.json", "x")

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
        createTask(name, weight)
        work_roulette()
    elif action == 'b':
        randomTask()
        work_roulette()
    elif action == 'c':
        searchAllTask()
        work_roulette()
    elif action == 'd':
        taskSelect = input("Which task are you searching for?").casefold()
        searchSingleTask(taskSelect)
        work_roulette()
    elif action == 'e':
        taskSelect = input("Which task do you want to remove?").casefold()
        removeTask(taskSelect)
        work_roulette()
    elif action == 'f':
        removeAllTasks()
        work_roulette()
    elif action == 'g':
        print('Goodbye!')

work_roulette()