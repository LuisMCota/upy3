"""
Team:
Luis Fernando Monterrubio Cota
Fátima Miranda Pestaña

With help of:
Christopher Cumi Llanes

"""
#import libraries
import numpy as np
import statistics
import os 
#Creation of the vector
Elements = int(input("Insert the number of elements: "))#The user inserts the quantity of values.
print(f"I am going to ask for {Elements} numbers:")#The user inserts the values.
Values =[]
value = []
for i in range(Elements):
        value = input(f"Insert the number {i + 1}: ")
        value = int(value)
        Values.append(value)

def menu(): #We defined a menu with the different operations.
    os.system("cls")
    print (" 1. add an element\n 2. eliminate an element \n 3. show the vector in a list \n 4. count elements \n 5. calculate the average and total of the elements \n 6.Exit\n")
    selection = int(input("Insert the number of what you want to do with the vector: "))

    if selection == 1:
        addition()
    elif selection == 2:
        eliminate()
    elif selection == 3:
        showing()
    elif selection == 4:
        counting()
    elif selection == 5:
        calculator()
    elif selection == 6: 
        salir()
    else:
        print("Error")

def return_menu():#We created the function to return to the menu and be able to work again with the same vector.
    selection2 = (int(input("Choose an option\n 1.Back to menu\n 2.Exit\n Answer: ")))
    if selection2 == 1:
        menu()
    else:
        return 0

def addition(): #We created the addition function
    NewValue = int(input("Insert the number to add:"))
    Values.append(NewValue)
    print(Values)
    return_menu()


def eliminate(): #We created the elimination function
    print(Values) 
    Eliminated =[]
    Eliminated = int(input("Insert the position of the value to eliminate (remember that is 0, 1, 2...)"))
    Values.pop(Eliminated)
    print(Values)
    return_menu()

def showing(): #We created the showing function
    from pprint import pprint
    pprint(Values, width=1)
    return_menu()

def counting(): #We created the counting function
    print(Values)
    repeticiones = {}
    for n in Values:
        if n in repeticiones :
            repeticiones[n] += 1
        else:
            repeticiones[n] = 0
    print(repeticiones)
    print(len(repeticiones))
    return_menu()

def calculator(): #We created the calculator function
    print(Values)
    mean = statistics.mean(Values)
    print("The mean is the following: ")
    print(mean)

    max_item = max(Values, key=int)
    print("The maximum element in the vector: ")
    print(max_item)
    return_menu()

def salir():
    return 0

menu()