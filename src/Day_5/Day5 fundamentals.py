#greeting message
def greet():
    print("Hello World!")
greet()
print()

#adding values
def add_numbers(a, b):
    return a+b
result = add_numbers(4, 5)
print(result)
print()

#Local and Global variables
icecream = "Chocolate"
def food():
    fruit = "Mango"
    vegetable = "Carrot"
    print("Fruit:",fruit)
    print("Vegetable:", vegetable)
    print("Icecream:", icecream)
food()
print()

#Modules
import math
import random
import datetime

number = 36
square_root = math.sqrt(number)
random_number = random.randint(1, 100) 
current_time = datetime.datetime.now()

print("Square root of", number, "is:", square_root)
print("Random number between 1 and 100:", random_number)
print("Current date and time:", current_time)



