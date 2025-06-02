#Variable = A container for a value (string, integer, float, boolean)
#A variable behaves as if it was the value it contains


#string
first_name = "Fidel"
food = "pizza"
email = "fidel@gmail.com"

print(first_name)
print("first_name")
print(f"Helo {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")


#integer
age = 25
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")


#float
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance}km")


#boolean
is_student = False 
for_sale = False
is_online = False

if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("That item is for sale")
else: 
    print("That item is not availble")

if is_online:
    print("You are online")
else:
    print("You are offline")

user_name = "Fidel"
year = 2024
pi = 3.14
is_admin = True

print(f"Hello everyone, my name is {user_name}")
print(f"I was born in {year}")
print(f"An example of a constant value is {pi}")
if is_admin:
    print("And yes, i'm an admin")
else:
    print("I'm unfortunately not an admin")