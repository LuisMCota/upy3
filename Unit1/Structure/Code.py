"""
PROJECT UNIT 2:

Daniel Valdes Artiles
Mariano Miranda 
Christian Can

The data is given in this form: M, N
AMOUNT 1 1 AMOUNT 1 2 ….. AMOUNT 1 N
AMOUNT 2 1 AMOUNT 2 2 ….. AMOUNT 2 N
AMOUNT M 1 AMOUNT M 2 ….. AMOUNT M N

Where:
M is an integer variable representing the number of years
between 1 and 30 inclusive.
N is an integer variable that represents the number of
company branches between 1 and 35 inclusive.
AMOUNT i j Real variable (2-dimensional matrix)
represents what was sold in year I at branch J.

The information that company directors need
to make decisions is as follows:
a. Branch that has sold the most in the M years.
b. Average sales per year.
c. Year with the highest average sales.
"""
#importando time para pausar el programa

import time

#Functions and classes.

class Array:
    def __init__(self, Years, Branches): # Rows = Years, Branch = Columns
        self.Years = Years
        self.Branches = Branches

# Asks the user to enter the data referring to the size of the matrix

def array_size():
    rows = int(input('Insert the years (1 : 30) you want to check: '))
    columns = int(input('Insert the number (1 : 35) of existing branches: '))

    if (rows > 30 or columns > 35):
        print('(System): los valores agregados no concuerdan con los datos existentes de la empresa, intente nuevamente...')
        array_size()

    return rows, columns # Returns the requested values

# Create the arrays to work with

def create_array(rows, column):
    # Array sum
    array = [] # Create an array to save the data
    for i in range(rows):
        year = i+1
        list = [] # Returns the list to empty to save more data without it accumulating
        for j in range(column):
            suc = j+1
            amount = float(input('Seld made in year '+ str(year) + ', branch ' + str(suc) + ' >>>  '))
            time.sleep(0.4)
            list.append(amount) # Insert values into a list
        array.append(list) # Insert the generated list into the array

    return array

# Function to recognize the maximum number of an array

def biggest_sale(Array, Years, branch): 
    value = Array[0][0] # Invokes the value 0.0 of the array as the basis of comparison
    value_year = 0 # Sets best selling year to 0
    value_bran = 0 # Sets the best-selling branch to 0
    for i in range(Years): # Starts a loop in years
        for j in range(branch): # Starts a loop in branches
            if Array[i][j] > value: # Asks if the value i,j is greater than the value assigned to value
                value = Array[i][j] # If it is greater, the value i,j is assigned to value
                value_year = i # Take the year of greatest value
                value_bran = j # Take the branch with the highest value

    return value, value_year+1, value_bran+1

# average sales in a specific year

def average_sales(array, year, branch):
    req_year = int(input('What year do you want to know the average sales?  ')) # asks the user for the required year
    print(" ")
    count = 0 # initialize the year to 0
    saveValue = 0 # initializes the vend value to 0
    for i in range(year): # starts a loop in years
        if (i+1 == req_year):
            for j in range(branch): # starts a loop in branches
                count = count+1 # count how many sales movements there are in that year
                saveValue = saveValue + array[i][j] # redeems the value of the sale sum

    
    mean = saveValue/count # determine the average sale
            
    return mean, req_year


# calculates the highest average sales in all years and returns the year with the highest average

def max_sale_av_year(array, year, branch):
    mean = 0 # starts the value to which the average will be assigned
    max_mean_year = 0 # start max year value
    for i in range(year): # Starts a loop in years
        count = 0 # starts the movement counter made in the years
        saveValue = 0 # start the variable that will store the added values
        for j in range(branch): # starts a loop in branches
            count = count+1 # count how many sales movements there are in that year
            saveValue = saveValue + array[i][j] # redeems the value of the sale sum

        meanPerYear = saveValue/count # determine the average sale
        if meanPerYear > mean:
            mean = meanPerYear # assigns the validated value to the variable to be returned
            max_mean_year = i # establishes which is the year with the highest sales average
    
            
    return mean, max_mean_year+1 # returns the year and the sales average


####################################################################################################################################

# User interface

# Generate and fill matrix

years, branch = array_size() 
array_Data = Array(years, branch) # creates an object of type Array
array1 =  create_array(array_Data.Years, array_Data.Branches)
rowM1 = array_Data.Years
columnM1 = array_Data.Branches

# Part a.

print('Array:  ' + str(array1))
max_sell, max_sell_year, max_sell_branch = biggest_sale(array1, rowM1, columnM1)
print('The biggest sale was ' + str(max_sell) + ' dollars in year ('+str(max_sell_year)+') in the branch ('+str(max_sell_branch)+')')
time.sleep(1)

# Part b.

av_sales, av_sales_year = average_sales(array1, rowM1, columnM1)
print('Average sales for the year '+ str(av_sales_year)+' is: '+str(av_sales))
time.sleep(1)

# Part c.

max_sale_av, max_year_av = max_sale_av_year(array1, rowM1, columnM1)
print('The year with the highest average sales is '+str(max_year_av)+ ' with an average sale of '+ str(max_sale_av) + ' dollars ')