import turtle
import random
from playsound import playsound

#<James Abela> (<01/22/22>) <wordle.py> (https://www.youtube.com/watch?v=UkiTW4BGb8o&t=26s)

def minecraftWords():
    file = open('minecraft_word.txt', 'r')

    fiveList=[]
    for line in file:
        for word in line.split():
            word = word.replace("(","").replace(")","")
            if len(word) == 5:
                fiveList.append(word)

    fiveList2 = []

    for i in fiveList:
        i = i.lower()
        if i not in fiveList2:
            fiveList2.append(i)
    number = random.randint(0, 93)
    word = fiveList2[number]
    return fiveList2

def fiveLetterWords():
    dictionary = open("five.txt", "r")

    fiveLetterList=[]
    for line in dictionary:
        for word in line.split():
            fiveLetterList.append(word)
    return fiveLetterList            

def lose():
    turtle.goto(-300, -200)
    turtle.speed(0)
    turtle.color("green")
    turtle.fillcolor("green")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(180)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.right(90)
    turtle.forward(180)
    turtle.left(90)
    turtle.forward(40)
    turtle.color("black")
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.pendown()
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(60)
    for i in range(3):
        turtle.left(90)
        turtle.forward(40)
    turtle.forward(100)
    for i in range(3):
        turtle.left(90)
        turtle.forward(40)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.end_fill()

    playsound('sound.wav')
    turtle.penup()
    turtle.goto(-100, -300)
    turtle.pendown()
    turtle.write("You died!", font =("Verdana", 42, "normal"))
    turtle.exitonclick()

word_list = ['stone', 'grass', 'plank', 'birch', 'water', 'glass', 'lapis', 'block', 'shrub', 'light', 'brown', 'green', 'black', 'poppy', 'azure', 'bluet', 'tulip', 'white', 'oxeye', 'daisy', 'brick', 'torch', 'chest', 'wheat', 'lever', 'plate', 'sugar', 'fence', 'mossy', 'melon', 'vines', 'table', 'stand', 'frame', 'cocoa', 'plant', 'ender', 'anvil', 'heavy', 'slime', 'lilac', 'peony', 'magma', 'flint', 'steel', 'apple', 'arrow', 'ingot', 'sword', 'stick', 'seeds', 'bread', 'boots', 'paper', 'watch', 'slice', 'steak', 'flesh', 'pearl', 'blaze', 'ghast', 'thick', 'night', 'cream', 'spawn', 'witch', 'sheep', 'squid', 'horse', 'polar', 'quill', 'baked', 'empty', 'shard', 'armor', 'fruit', 'totem', 'shell', 'music', 'biome', 'swamp', 'taiga', 'ocean', 'hills', 'caves', 'world', 'smite', 'flame', 'power', 'speed', 'curse']
answer = random.choice(word_list) 
y = 350 
turtle.speed(0)

screen = turtle.Screen()
screen.screensize(300, 100000)

def draw_square(x,y,col): # x,y coordinates and a color
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(col) # set the fillcolor
    turtle.begin_fill()     # start the filling color
    for i in range(4): 
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill() # ending the filling of the color

def searchText(guess):
    file = open("five.txt", "r")
    file = file.read()
    if guess in file or guess in word_list:
        return True
    else:
        return False

def input_guess(prompt):
    
    my_input = turtle.textinput("5 letter word", prompt)
    dictionary = fiveLetterWords()
    while my_input == None: 
        my_input = turtle.textinput("Enter 5 letter word", prompt) # if you press cancel or submit with nothing
    while len(my_input) != 5: 
         my_input = turtle.textinput("Enter valid word", prompt)
    while searchText(my_input) == False:
        my_input = turtle.textinput("Enter valid word", prompt)
    return my_input.lower() 

def check_guess(my_input,answer,y):
    count = 0 
    x = -250 
    for i in my_input:
        if i == answer[count]: draw_square(x,y,"green") #exact character match draws a green square
        elif i in answer: draw_square(x,y,"yellow") #else if character anywhere in word draws yellow
        else: draw_square(x,y,"red") # otherwise draws red
        count+=1 
        x += 75 
    turtle.penup()
    turtle.goto(x,y-25) #Moves it slightly down for the word
    turtle.write(my_input,font=("Verdana", 15, "normal")) 

def play():
    
    print("Welcome to Minecraft Wordle!")
    print("Guess the Minecraft word!")
    print("This game has several has two game modes, survival and creative.")
    print("Creative mode gives you unlimited chances to guess the word.")

    gamemode = input("Which gamemode would you like to play in? (Enter creative or survival): ")

    gamemode = gamemode.lower()
    y = 350

    while gamemode not in ["creative", "survival"]:
        gamemode = input("Enter a valid gamemode to play in (survival or creative): ")
    else:
        if gamemode == "creative":
            guess_prompt = ("What is your guess?")
            my_input = input_guess(guess_prompt)
            if my_input == answer:
                turtle.penup()
                turtle.goto(-300,-200) 
                turtle.write("Well Done!",font=("Verdana", 42, "normal"))
            else:
                turtle.penup()
                turtle.goto(-300,-200)
                check_guess(my_input,answer,y)
                while my_input != answer:
                    my_input = input_guess(guess_prompt)
                    y -= 75
                    check_guess(my_input,answer,y)
                    if my_input == answer:
                        turtle.penup()
                        turtle.goto(-300,-200) 
                        turtle.write("You win!",font=("Verdana", 42, "normal"))
                        playsound('level.wav')
                        turtle.exitonclick()

        elif gamemode == "survival":
            hardcoreMode = input("Would you like to play in hardcore (one try)? (Enter yes or no): ")
            hardcoreMode = hardcoreMode.lower()
            while hardcoreMode not in ["yes", "no"]:
                hardcoreMode = input("Enter yes or no: ")
            else:
                if hardcoreMode == "yes":
                    for i in range(1): 
                        guess_prompt = "What is guess "+str(i+1)+"?" 
                        my_input = input_guess(guess_prompt) 
                        check_guess(my_input,answer,y)  
                        y -= 75 
                        if my_input == answer:
                            turtle.penup()
                            turtle.goto(-300,-200) 
                            turtle.write("You win!",font=("Verdana", 42, "normal"))
                            playsound('level.wav')
                            turtle.exitonclick()
                    else: 
                        turtle.penup()
                        turtle.goto(-300,-200)
                        turtle.write(answer,font=("Verdana", 42, "normal"))
                        turtle.goto(-300, -250)
                        lose()
                elif hardcoreMode == "no":
                    for i in range(6): 
                        guess_prompt = "What is guess "+str(i+1)+"?" 
                        my_input = input_guess(guess_prompt) 
                        check_guess(my_input,answer,y)  
                        y -= 75 
                        if my_input == answer:
                            turtle.penup()
                            turtle.goto(-300,-200) 
                            turtle.write("You win!",font=("Verdana", 42, "normal"))
                            playsound('level.wav')
                            turtle.exitonclick()
                    else: 
                        turtle.penup()
                        turtle.goto(-300,-200)
                        turtle.write(answer,font=("Verdana", 42, "normal"))
                        turtle.goto(-300, -250)
                        lose()

play()
