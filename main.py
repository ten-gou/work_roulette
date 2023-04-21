from verify import verify
from task_functions import createTask, randomTask, searchAllTask, searchSingleTask, removeTask

print('What would you like to do?')
print('[A] Add a new task') #CreateTask
print('[B] Choose a random task') #RandomTask
print('[C] See the full task list') #SearchAllTask
print('[D] Check for an individual task') #SearchSingleTask
print('[E] Delete a task') #RemoveTask
action = verify(5)

if action == 'a':
    print("Input the new task that you would like to add to the list:")
    createTask(input())
elif action == 'b':
    randomTask()
elif action == 'c':
    searchAllTask()
elif action == 'd':
    print("Which task are you searching for?")
    taskSelect = input().casefold()
    searchSingleTask(taskSelect)
elif action == 'e':
    print("Which task do you want to remove?")
    taskSelect = input().casefold()
    removeTask(taskSelect)