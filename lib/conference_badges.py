def badge_maker(name):
    return "Hello, my name is " + name + "."

def batch_badge_creator(names):
    list = []
    for name in names:
        list.append("Hello, my name is " + name + ".")
    return list

def assign_rooms(names):
    room = 0
    list = []
    for name in names:
        room += 1
        list.append("Hello, " + name + "! You'll be assigned to room " + str(room) + "!") 
    return list
    
def printer(names):
    for name in batch_badge_creator(names): 
        print(name)
    for assignment in assign_rooms(names):
        print(assignment)