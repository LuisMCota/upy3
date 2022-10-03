import pandas as pd
print('----------- WELCOME TO THE LAB ------------')
print('Lets create a mutant animal!')
class animals():
    count = 0
    def __init__(self):
        self.especie = str(input('\nName of the specie => '))
        self.IQ = int(input('Enter the IQ => '))
        self.habilitie_1 = str(input('Enter your habilities => '))
        self.habilitie_2 = None
        animals.count += 1

    def prints(self):
        data = {'Name':[self.especie],
                'IQ':[self.IQ],
                'Habilitie 1':[self.habilitie_1],
                'Habilitie 2':[self.habilitie_2]}
        df  = pd.DataFrame(data)
        print(df)

animal_1 = animals()
animal_2 = animals()
animal_3 = animals() 
animal_1.prints()
animal_2.prints()
animal_3.prints()

def superior_intelligence(iq_animal, specie):
    answer = int(input('\nHow much you want to increase your iq? '))
    iq_animal = answer + iq_animal
    print('\n',specie, 'have now', iq_animal, 'of iq')

def pinkify(habilities):
    answer = str(input('You want to eliminate all the habilities? '))
    if answer == 'yes':
        habilities = habilities.split(' ').pop(len(habilities.split(' '))-1) 
        print(habilities)
    else:
        print('OK')

def super_power(especie, habilities_2, iq_animal):
    if especie == 'elephant':
        habilities_2 = 'Not be afraid of mice!'
        
    elif especie == 'mouse' and iq_animal > 100:
        habilities = 'Speak'
        print(habilities)
    else:
        print('Regresa al menu')


answer = str(input('\nDo you want to transform one of the animals? '))
if answer == 'yes':
    print('\n----------- TRANSFORMATION -----------')
    question_1 = int(input('\nWhat do you want to transform?\n 1. Superior Intelligence\n 2. Pinkify\n 3. Super powers\n 4. Exit\n'))
    while question_1 != 4:
        if question_1 == 1:
            print('\n ----------- INTELLIGENCE ----------')
            question_2 = int(input('\nChoose an animal:\n 1. Experimento 1\n 2. Experimento 2\n 3. Experimento 3\n 4. Regresar\n'))
            while question_2 != 4:
                if question_2 == 1:    
                    superior_intelligence(animal_1.IQ, animal_1.especie)
                elif question_2 == 2:
                    superior_intelligence(animal_2.IQ,animal_2.especie)
                elif question_2 == 3:
                    superior_intelligence(animal_3.IQ,animal_3.especie)
                else:
                    print('Put a correct animal')  
                question_2 = int(input('\nChoose an animal:\n 1. Experimento 1\n 2. Experimento 2\n 3. Experimento 3\n 4. Regresar\n'))
        elif question_1 == 2:
            print('\n----------- PINKIFY -----------')
            question_3 = int(input('\nChoose an animal:\n 1. Experimento 1\n 2. Experimento 2\n 3. Experimento3\n 4. Regresar\n'))
            while question_3 != 4:
                if question_3 == 1:  
                    pinkify(animal_1.habilitie_1)  
                elif question_3 == 2:
                    pinkify(animal_2.habilitie_1)  
                elif question_3 == 3:
                    pinkify(animal_3.habilitie_1)  
                else:
                    print('Put a correct animal')  
                question_3 = int(input('\nChoose an animal:\n 1. Experimento 1\n 2. Experimento 2\n 3. Experimento 3\n 4. Regresar\n')) 
        elif question_1 == 3:
            print('\n----------- SUPER POWERS -----------')
            question_4 = int(input('\nChoose an animal:\n 1. Experimento 1\n 2. Experimento 2\n 3. Experimento 3\n 4. Regresar\n'))
            while question_4 != 4:
                if question_4 == 1: 
                    super_power(animal_1.especie, animal_1.habilitie_2, animal_1.IQ) 
                    animal_1.prints()
                elif question_4 == 2:
                    pinkify(animal_2.habilitie_1)  
                elif question_4 == 3:
                    pinkify(animal_3.habilitie_1)  
                else:
                    print('Put a correct animal')  
                question_4 = int(input('\nChoose an animal:\n 1. Experimento 1\n 2. Experimento 2\n 3. Experimento 3\n 4. Regresar\n'))
            
        else:
            print('')
        question_1 = int(input('\nWhat do you want to transform?\n 1. Superior Intelligence\n 2. Pinkify\n 3. Super powers\n 4. Exit\n'))
else:
    print('')
        
