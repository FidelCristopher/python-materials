# 2Dlist = [list1, list2, list3]

# fruits =     ["apple", "orange", "banana", "coconut"] 
# vegetables = ["celery", "carrots", "potatoes"]
# meats =      ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

# # print(groceries[0][0]) 
# # print(groceries[1][0])

# for collection in groceries: 
#     for food in collection: 
#         print(food, end=" ")
#     print()


# -------------------
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()