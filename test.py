import random
# GET GUESS
def getGuess():
    return list(input("What is your guess? "))
# GENERATE COMPUTER CODE 123
def generateCode():
    digits = [str(num) for num in range(10)]
    #Shuffle the digits
    random.shuffle(digits)
    
    # Then grab the first three
    return digits[:3]
# GENERATE THE CLUES
def generateClues(code,userGuess):

    if userGuess == code:
        return "CODE CRACKED"

    clues = []

    for ind, num in enumerate(userGuess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")
    if clues == []:
        return ["Nope"]
    else:
        return clues
# RUN GAME LOGIC
print("Welcome Code Breaker!")
secretCode = generateCode()
clueReport = []
while clueReport != ["CODE CRACKED"]:
    guess = getGuess()
    clueReport = generateClues(guess,secretCode)
    for clue in clueReport:
        print(clue)
