import random
import json

def menu():
    print("\n----- Movie Selector 9000 ------")
    print("1) Choose random movie\n2) View list\n3) Add movie\n4) Remove movie")
    return input("")

def loadJson():
    with open("data.json") as json_file:
        data = json.load(json_file)
    return data

def writeJson(data):
    with open("data.json", "w") as outfile:
        json.dump(data, outfile)

def viewMovie():
    data = loadJson()
    listMovie()
    print("View details of movie")
    print("C to exit")
    while True:
        try:
            command = input("")
            if command == "c":
                break
            elif int(command) <= len(data)-1 and int(command) >= 0:
                data = loadJson()
                name = data[int(command)]["name"]
                score = data[int(command)]["score"]
                runtime = data[int(command)]["runtime"]
                line()
                print("{0}\nScore: {1}\nRuntime: {2}".format(name,score,runtime))
                break
        except ValueError:
            print("Not recognised")
            break
    
def listMovie():
    data = loadJson()
    p = 0
    line()
    for x in data:
        print("{0}) {1}".format(p,x["name"]))
        p += 1
    line()

def randomMovie():
    data = loadJson()
    num = random.randint(0,len(data))
    line()
    print(data[num]["name"])
    line()

def removeMovie():
    listMovie()
    answer = int(input("What movie would you like to remove?\n"))
    data = loadJson()
    del data[answer]
    writeJson(data)
    
def addMovie():
    name = input("What is the name of the movie?\n")
    score = input("What is the score of the movie?\n")
    runtime = input("What is the runtime of the movie?\n")
    data = loadJson()
    data.append({"name":name,"score":score,"runtime":runtime})
    writeJson(data)
    print("Movie added!")
    
def line():
    print("--------------------------------")

while True:
    choice = menu()
    if choice == "1":
        randomMovie()
    elif choice == "2":
        viewMovie()
    elif choice == "3":
        addMovie()
    elif choice == "4":
        removeMovie()
    else:
        print("Answer not recognised")
