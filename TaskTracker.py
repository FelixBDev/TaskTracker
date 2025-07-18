import sys
class Task:
    def __init__(self, name, status):
        self.name = name
        self.status = status
    
    def __str__(self):
        return f"Task : {self.name} || Status : {self.status}"

allTask = []
numOfTask = 0

#Information sur comment marche l'application
print('What do you want to do?')
print('If you want to add a task write : add')
print('If you want to update a task write : update')
print('If you want to remove a task write : remove')
print('If you want to see your list simply write : list')
print('If you want to exit simply write : exit')



#Ajouter une nouvelle tache
while True:
    try:
        userAction = input('> ')
        if userAction == 'add':
            print('Please write the name of the task.')
            
            taskName = input('> ')
            allTask.append(Task(taskName, 'To do'))


        elif userAction == 'remove':

            print('Please write the name of the task you want to remove')

            taskToRemove = input('> ')
            for i in allTask:
                if i.name == taskToRemove:
                    allTask.remove(i)
                    print('Task is removed.')
                else:
                    print('Task not found')

        elif userAction == 'update':
            print('Please write the name of the task you want to update')
            taskToUpdate = input('> ')
            for i in allTask:
                if i.name == taskToUpdate:
                    print('Changing the task ' + i.name)
                    print('Write the new status.')
                    i.status = input('> ')

        elif userAction == 'list':
            for i in allTask:
                print(i)
        

        elif userAction == 'exit':
            sys.exit()
    
        else:
            print('Not sure this is an adequate response, please write a valid response.')

    except ValueError:
        print('Seems this task does not exist yet.')