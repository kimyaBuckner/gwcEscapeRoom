from PIL import Image

userName = ""
ready = False


def getPlayerName():
    global userName
    userName = raw_input("What is your name?\n")
    print("Hi " + userName + " are you ready to play the game?\n")


def readyToStart():
    global ready
    response = raw_input("Type Y for yes type N for no\n")

    if(response == "Y"):
        print("Let's start now")
        ready = True
    else:
        raw_input("ype Y when reasy to start \n")


def beginngContext():
    global ready
    if ready==True:
        print("Mary was found dead in her bedroom. The police gave you some information.\n 1. They know that she was 32 years old. She was the CEO of the Champion company.\n 2. They sent you some photos of her corpse. \n 3. She also had several messages from an unknown contact and they seemed to be using a code. ")

# def giveOptions():

def listSuspects():
    suspectOne = "Janette -- Mary's best friend. She was the last person to speak to Mary\n"
    suspectTwo = "Robert -- Mary's ex-boyfriend. They broke up after an argument. About two weeks ago. She has a restraining order against him.\n"
    suspectThree = "Kate -- Mary's sister. She wanted to be the CEO of the company. She was upset when she was not chosen\n"

    print("\n\nThese are the current suspects in Mary's death: \n\n")
    print(suspectOne)
    print(suspectTwo)
    print(suspectThree)

def challenge():
    global userName
    print("\nIt's up tp Detective " + userName + " to solve the case of her murder\n")

def userOptions():

    optionOne = "See more clues (type 1) "
    optionTwo = "Look at the pictures (type 2) "
    optionThree = "End the game (type 3)"

    print("What would you like to do?\n")
    print(optionOne +"\n"+ optionTwo +"\n"+ optionThree)
    response = raw_input("")

    if(response == "1"):
        print ("more clues")
    elif (response == "2"):
        showImage("C:/Users/kimya/OneDrive/Desktop/img.png")
    else:
        print ("game over")

def showImage(url):
    image = Image.open(url)
    image.show()

def gameLogic():
    getPlayerName()
    readyToStart()
    beginngContext()
    listSuspects()
    challenge()
    userOptions()

# gameLogic()
gameLogic()
