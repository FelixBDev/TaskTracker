import sys
import json
import os
import time


class Task:
    def __init__(self, id, name, status, heure_creation, heure_modification):
        self.id = id
        self.name = name
        self.status = status
        self.heure_creation = heure_creation
        self.heure_modification = heure_modification

    def __str__(self):
        return f"Task : {self.name} || Status : {self.status}"
    
    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'status': self.status, 'heure_creation': self.heure_creation, 'heure_modification': self.heure_modification}

    @classmethod
    def from_dict(cls, data):
        return cls(data['id'], data['name'], data['status'], data['heure_creation'], data['heure_modification'])

FILE_PATH = 'tasks.json'

def load_tasks():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as f:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]
    return []

# Sauvegarder les tâches dans le fichier
def save_tasks(tasks):
    with open(FILE_PATH, 'w') as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)




allTask = load_tasks()
numOfTask = len(allTask)

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
        #AJOUT DE TACHE
        userAction = input('> ')
        if userAction == 'add':
            print('Please write the name of the task.')
            
            taskName = input('> ')
            allTask.append(Task(numOfTask, taskName, 'to do', time.ctime(), time.ctime()))
            numOfTask = numOfTask + 1
            save_tasks(allTask)

        #ENLEVER UNE TACHE
        elif userAction == 'remove':

            print('Please write the name of the task you want to remove')

            taskToRemove = input('> ')
            for i in allTask:
                if i.name == taskToRemove:
                    allTask.remove(i)
                    save_tasks(allTask)
                    print('Task is removed.')
                else:
                    print('Task not found')
        #MODIFICATION DE STATUS DE TACHE
        elif userAction == 'update':
            print('Please write the name of the task you want to update')
            taskToUpdate = input('> ')
            for i in allTask:
                if i.name == taskToUpdate:
                    print('Changing the task ' + i.name)
                    print('Write the new status : to do, done, finished')
                    save_tasks(allTask)
                    i.status = input('> ')
        #LISTE TOUT LES TACHES
        elif userAction == 'list':
            for i in allTask:
                print(i)
        elif userAction == 'list done':
            for i in allTask:
                if i.status == 'done':
                    print(i)
        elif userAction == 'list finished':
            for i in allTask:
                if i.status == 'finished':
                    print(i)
        elif userAction == 'list to do':
            for i in allTask:
                if i.status == 'to do':
                    print(i)
        
        #QUITTE L'APPLICATION
        elif userAction == 'exit':
            sys.exit()
    
        else:
            print('Not sure this is an adequate response, please write a valid response.')

    except ValueError:
        print('Seems this task does not exist yet.')