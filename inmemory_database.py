import json
database = {}
print("Syntax : <Command> <Key> <Value>")

while True:
    userinput = input()
    listinput = userinput.split() 
    '''database[listinput[1]] = listinput[2]
    print(database)'''
    if len(listinput) == 0:
        print("Invalid Input")
        continue



    if listinput[0] == "SET":
        if len(listinput) == 1:
            print("Invalid Input")
            continue
        if len(listinput) == 2:
            print("You forgot to assign a value to the key.")
            continue
        database[listinput[1]] = listinput[2]



    elif listinput[0] == "EXIT":
        break



    elif listinput[0] == "GET":
        if len(listinput) == 1:
            print("Invalid Input")
            continue
        if listinput[1] in database:
            print(database[listinput[1]])
        else: 
            print("Key doesn't exist.")



    elif listinput[0]=="DEL":
        if len(listinput) == 1:
            print("Invalid Input")
            continue
        if listinput[1] in database:
            database.pop(listinput[1])
        else:
            print("Key doesn't exist or has been deleted.")



    elif listinput[0] == "EXISTS":
        if len(listinput) ==1:
            print("Invalid Input")
            continue
        if listinput[1] in database:
            print(1)
        else:
            print(0)



    elif listinput[0] == "SAVE":
        if len(listinput) ==1:
            print("Invalid Input")
            continue
        f = open(listinput[1], "w")
        f.write(json.dumps(database))
        f.close()
    


    elif listinput[0] == "LOAD":
        if len(listinput) ==1:
            print("Invalid Input")
            continue
        try: 
            f = open(listinput[1], "r")
            dbcontent = f.read()
            f.close()
            print("Database has been loaded.")
            database = json.loads(dbcontent)
        except:
            print("Database either not found or doesn't contain valid JSON data.")



    else:
        print("Invalid Input")