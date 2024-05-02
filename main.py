import json

n = 5
friends = {}


def add_friends(first, second):
    global friends
    if first not in friends:
        friends[first] = []

    if second not in friends:
        friends[second] = []

    friends[first].append(second)
    friends[second].append(first)


def export_to_json():
    with open("friends.json", "w") as file:
        json.dump(friends, file, indent=4)


def import_from_json():
    global friends
    with open("friends.json", "r") as file:
        friends = json.load(file)
    return friends


for _ in range(n):
    first_name, second_name = input("Enter two people name divided by spaces: ").split()
    add_friends(first_name, second_name)

export_to_json()
print(import_from_json())
