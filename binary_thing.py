'''import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

length = len(countries)
print(countries[1])
print(countries)

# Start your search algorithm here.'''

#SOBS DRAMATICALLY

'''nums=[1,2,3,4,5,6,7,8,9]
my_num=(int(input("What number do you want to test?")))
nums_to_check = nums

while len(nums_to_check)>0:
    length = len(nums_to_check)/2
    test_spot=nums_to_check[int(length)]
    print("test_spot is:", test_spot)
    if my_num == test_spot:
        print("Your number", my_num," is in the list")
        nums_to_check = []
    elif my_num < test_spot:
        nums_to_check = nums_to_check[:test_spot]
    elif my_num > test_spot:
        nums_to_check = nums_to_check[test_spot:]
    print(nums_to_check)

print('Yay!')'''

import time

animals=["alligator", "bumblebee", "cow", "dog", "elephant", "fruit fly", "giraffe", "horse", "iguana", "jaguar", "koala", "llama", "moose"]
my_animal=(input("What animal do you want to test?"))
animals_to_check = animals

while len(animals_to_check)>0:
    length = int(len(animals_to_check)/2)
    test_spot=animals_to_check[int(length)]
    print("test_spot is:", length)
    if my_animal == test_spot:
        print("Your number", my_animal," is in the list")
        animals_to_check = []
    elif test_spot[0] == my_animal[0]:
        for i in range(len(my_animal)):
            if test_spot[i] != my_animal[i]:
                if my_animal[i] < test_spot[i]:
                    animals_to_check = animals_to_check[:length]
                elif my_animal[i] > test_spot[i]:
                    animals_to_check = animals_to_check[length:]
    elif my_animal < test_spot:
        animals_to_check = animals_to_check[:length]
    elif my_animal > test_spot:
        animals_to_check = animals_to_check[length:]
    print(animals_to_check)
    time.sleep(2)
    
    
print('Yay!')
'''put into a function and ply around with using return true and if it doese not work it is not in the function'''    