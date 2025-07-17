import sys
class Task:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return f"Task : {self.name}, status : {self.status})"

allTask = [Task]
numOfTask = 0

#Information sur comment marche l'application
print('What do you want to do?')
print('If you want to add a task write : new task')
print('If you want to update a task write : update task')
print('If you want to remove a task write : remove task')
print('If you want to see your list simply write : to do list')
print('If you want to exit simply write : exit')



#Ajouter une nouvelle tache
while True:
    try:
        userAction = input('> ')
        if userAction == 'new task':
            print('Please write the name of the task.')
            
            taskName = input('> ')
            globals()[f"task{numOfTask}"] = Task(taskName, 'To do')
            allTask.append(Task(taskName, 'To do'))
            numOfTask = numOfTask + 1


        elif userAction == 'remove task':
            print('Please write the name of the task you want to remove')
            allTask.remove(input('> '))
            print('Your current task are ' + str(allTask))

        elif userAction == 'update task':
            print('Please write the name of the task you want to update')
            allTask.remove(input('> '))
            print('What do you want it to say now?')
            allTask.append(input('> '))

            print('Your current task are ' + str(allTask))

        elif userAction == 'to do list':
            for i in allTask:
                print(i)
        

        elif userAction == 'exit':
            sys.exit()
    
        else:
            print('Not sure this is an adequate response, please write a valid response.')

    except ValueError:
        print('Seems this task does not exist yet.')