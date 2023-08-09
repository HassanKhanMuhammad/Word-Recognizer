userInput1 = input("File: ")
userInput2 = input("Word: ")

with open(userInput1, "r") as f:
    content = f.read()
    if userInput2 or userInput2.lower() in content:
        print(f"{userInput2} is in {userInput1}")
    else:
        print(f"{userInput2} is not in {userInput1}")
