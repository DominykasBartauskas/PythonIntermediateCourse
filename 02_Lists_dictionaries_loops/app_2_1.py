list = ["Spiderman", "Ironman", "Thor", "Groot"]
dict = {
    "hero_name": "Spiderman",
    "name": "Peter Parker",
    "race": "Human",
    "group": "Avengers"
}

print(list[2])
list.append("Gamora")
list.remove("Groot")
list[1] = "Tony Stark"

print(dict["name"])
dict["age"] = 21
dict.pop("group")
dict["group"] = "None"

print(list)
print(dict)
