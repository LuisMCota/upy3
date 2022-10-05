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

def superior_intelligence(animal):
    answer = int(input('\nHow much you want to increase your iq? '))
    animal.IQ = answer + animal.IQ
    print(animal.especie, 'have now', animal.IQ, 'of iq')

def pinkify(animal):
    answer = str(input('You want to eliminate all the habilities? '))
    if answer == 'yes':
        animal.habilitie_1 = None
        animal.habilitie_2 = None
        animal.prints()
    else:
        print('Going back...')

def super_power(animal):
    if animal.especie == 'elephant':
        animal.habilitie_2 = 'Not be afraid of mice!'
        animal.prints()
    elif animal.especie == 'mouse' and animal.IQ > 100:
        animal.habilitie_2 = 'Speak'
        animal.prints()
    else:
        print('Going back...')

def criteria(animal):
    if animal.habilitie_2 == 'speak' or animal.IQ > 60:
        print(animal.especie, 'is anthropomorfic!\nIt is suitable for experimentation!')
    else:
        print(animal.especie, 'is not anthropomorfic!\nNot suitable for experimentation!')

def not_So_Sane():
    inp = str(input('Put the pinkieska word => '))
    def contar_vocales(input):
        contador = 0
        for letra in input:
            if letra.lower() in "aeiouAEIOU":
                contador += 1
        return contador

    output = contar_vocales(inp)
    if len(inp) <= 4 and output == 1:
        print('Do', inp,'!!!','\nTRUE')
    else:
        print('It is not a pinkiesca word')



answer = str(input('\nDo you want to transform one of the animals? '))
if answer == 'Yes' or answer == 'yes' or answer == 'Y' or answer == 'y':
    print('\n----------- TRANSFORMATION -----------')
    question_1 = int(input('\nWhat do you want to transform?\n 1. Superior Intelligence\n 2. Pinkify\n 3. Super powers\n 4. Exit\n'))
    while question_1 != 4:
        if question_1 == 1:
            print('\n ----------- INTELLIGENCE ----------')
            question_2 = int(input('\nChoose an animal:\n 1. Experimento 1\n 2. Experimento 2\n 3. Experimento 3\n 4. Regresar\n'))
            while question_2 != 4:
                if question_2 == 1:    
                    superior_intelligence(animal_1)
                elif question_2 == 2:
                    superior_intelligence(animal_2)
                elif question_2 == 3:
                    superior_intelligence(animal_3)
                else:
                    print('Put a number of the list!!!')  
                question_2 = int(input('\nChoose an animal:\n 1. Experiment 1\n 2. Experiment 2\n 3. Experiment 3\n 4. Regresar\n'))
        elif question_1 == 2:
            print('\n----------- PINKIFY -----------')
            question_3 = int(input('\nChoose an animal:\n 1. Experiment 1\n 2. Experiment 2\n 3. Experiment 3\n 4. Regresar\n'))
            while question_3 != 4:
                if question_3 == 1:  
                    pinkify(animal_1)
                elif question_3 == 2:
                    pinkify(animal_2)  
                elif question_3 == 3:
                    pinkify(animal_3)  
                else:
                    print('Put a number of the list!!!')  
                question_3 = int(input('\nChoose an animal:\n 1. Experiment 1\n 2. Experiment 2\n 3. Experiment 3\n 4. Regresar\n'))
        elif question_1 == 3:
            print('\n----------- SUPER POWERS -----------')
            question_4 = int(input('\nChoose an animal:\n 1. Experiment 1\n 2. Experiment 2\n 3. Experiment 3\n 4. Regresar\n'))
            while question_4 != 4:
                if question_4 == 1: 
                    super_power(animal_1)
                elif question_4 == 2:
                    super_power(animal_2) 
                elif question_4 == 3:
                    super_power(animal_3) 
                else:
                    print('Put a number of the list!!!')  
                question_4 = int(input('\nChoose an animal:\n 1. Experiment 1\n 2. Experiment 2\n 3. Experiment 3\n 4. Regresar\n'))
        else:
            print('Put one number of the list!!!')
        question_1 = int(input('\nWhat do you want to transform?\n 1. Superior Intelligence\n 2. Pinkify\n 3. Super powers\n 4. Exit\n'))
else:
    print('OKAY CONTINUE...')

ans_1 = str(input('\nDo you want to know if your animal is suitable for transformation? '))
if ans_1 == 'Yes' or ans_1 == 'yes' or ans_1 == 'Y' or ans_1 == 'y':
    ans_2 = int(input('\nChoose an animal:\n 1. Experiment 1\n 2. Experiment 2\n 3. Experiment 3\n 4. Exit\n'))
    while ans_2 != 4:
        if ans_2 == 1:
            criteria(animal_1)
        elif ans_2 == 2:
            criteria(animal_2)
        elif ans_2 == 3:
            criteria(animal_3)
        else:
            print('Put one number of the list! ')
        ans_2 = int(input('\nChoose an animal:\n 1. Experiment 1\n 2. Experiment 2\n 3. Experiment 3\n 4. Exit\n'))
else:
    print('ITS IMPORTANT TO KNOW THIS!!\n')

print('\nTo continue, create a pinkiesca word!')
not_So_Sane()

print('\n------------------- RESULTS -------------------\n')
animal_1.prints()
print()
criteria(animal_1)
print('-----------------------------------------------')
animal_2.prints()
print()
criteria(animal_2)
print('-----------------------------------------------')
animal_3.prints()
print()
criteria(animal_3)