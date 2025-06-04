# dictionary = a collection of {key:value} pairs 
#                 ordered and changeables. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))

# if capitals.get("Russia"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exists")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detriot"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#     print(values)

# items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")