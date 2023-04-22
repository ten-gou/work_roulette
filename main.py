from verify import verify
from task_functions import createTask, randomTask, searchAllTask, searchSingleTask, removeTask

def main():
    print('What would you like to do?')
    print('[A] Add a new task') #CreateTask
    print('[B] Choose a random task') #RandomTask
    print('[C] See the full task list') #SearchAllTask
    print('[D] Check for an individual task') #SearchSingleTask
    print('[E] Delete a task') #RemoveTask
    print('[F] End function')
    action = verify(6)

    if action == 'a':
        name = input("Input the new task that you would like to add to the list:")
        weight = input("Input the weight/importance of the task:")
        createTask(name, weight)
        main()
    elif action == 'b':
        randomTask()
        main()
    elif action == 'c':
        searchAllTask()
        main()
    elif action == 'd':
        taskSelect = input("Which task are you searching for?").casefold()
        searchSingleTask(taskSelect)
        main()
    elif action == 'e':
        taskSelect = input("Which task do you want to remove?").casefold()
        removeTask(taskSelect)
        main()
    elif action == 'f':
        print('Goodbye!')

main()