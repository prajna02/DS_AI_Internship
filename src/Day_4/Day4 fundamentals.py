# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 11:19:59 2026

@author: DELL
"""

#Dictionaries
Student = {"name":"Pruthvi",
           "age":22,
           "course":"Data Science"
           }
print(Student["name"])
Student["age"]=22
Student["city"]="Delhi"
print(Student)
print()


#dictionary methods and iteration
marks={"math":80,"science":75,"english":85}
print(marks.get("math"))
print(marks.get("history",0))
for subject,score in marks.items():
    print(subject,score)
marks.update({"kannada":90})
print(marks)
marks.pop("math")
print(marks)
print()


#Using loop
purchases = {"Pruthvi": 350,
             "Prajna": 250,
             "Priya":340
            }
for name, amount in purchases.items():
    print(f"{name} spent ₹{amount}")
print()    
    
    
#With User input
n=int(input("Enter number of customers:"))
user_purchases = {}
for i in range(n):
    name = input("Enter customer name:")
    amount = int(input("Enter the amount:"))
    user_purchases[name]=amount
print("Customer purchase data:", user_purchases)
#Using max() for key
top_customer = max(purchases, key=purchases.get)
print("Maximum spending customer:", top_customer)

#Using min() for key
top_customer = min(purchases, key=purchases.get)
print("Minimum spending customer:", top_customer)

