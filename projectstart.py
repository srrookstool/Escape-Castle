import os
import time

def printTitle():
   print("""
░█▀▀░█▀▀░█▀▀░█▀█░█▀█░█▀▀░░░▀█▀░█░█░█▀▀░░░█▄█░█▀▀░█▀▄░▀█▀░█░█░█▀▀░█░█░█▀█░█░░░░░█▀▀░█▀█░█▀▀░▀█▀░█░░░█▀▀
░█▀▀░▀▀█░█░░░█▀█░█▀▀░█▀▀░░░░█░░█▀█░█▀▀░░░█░█░█▀▀░█░█░░█░░▀▄▀░█▀▀░▀▄▀░█▀█░█░░░░░█░░░█▀█░▀▀█░░█░░█░░░█▀▀
░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░░░▀▀▀░░░░▀░░▀░▀░▀▀▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░░▀░░▀▀▀░░▀░░▀░▀░▀▀▀░░░▀▀▀░▀░▀░▀▀▀░░▀░░▀▀▀░▀▀▀
""")

# singleton - only one player
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.inv = []
        self.position = None
        self.timeRemaining = 1800
    
    def checkInventory(self):
        pass
    
    def addItemInventory(self,item):
        pass
    
    def modTime(self, minutes):
        self.timeRemaining += minutes * 60
        pass
    
    def restoreTime(self):
        self.timeRemaining = 1800

    def checkGameState(self, challenges):
        # WIN CONDITION:
        if all(ch.isCompleted for ch in challenges):
            print("You ESCAPED!")
            return True

        # LOSE CONDITION: timer ran out
        if self.timeRemaining <= 0:
            print("""░▀█▀░▀█▀░█▄█░█▀▀░█▀▀░░░█░█░█▀█░█░░░█░█░█▀█░█░█░░░█░░░█▀█░█▀▀░█▀▀░█
                     ░░█░░░█░░█░█░█▀▀░▀▀█░░░█░█░█▀▀░▀░░░░█░░█░█░█░█░░░█░░░█░█░▀▀█░█▀▀░▀
                     ░░▀░░▀▀▀░▀░▀░▀▀▀░▀▀▀░░░▀▀▀░▀░░░▀░░░░▀░░▀▀▀░▀▀▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀""")
            return True

        # Game continues
        return False
    

class Object:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def examine(self):
        pass

class Pickup(Object):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.isPickedUp = False
        
    def pickUp(self):
        pass
    
    def putBack(self):
        pass
        
    
class Clue(Pickup):
    def __init__(self, name, description):
        super().__init__(name,description)
        self.isInspected = False
    
    def examine(self):
        super().examine()
        self.isInspected = True
    
    def isClue(self):
        pass

class Puzzle(Object):
    def __init__(self,name,description):
        super().__init__(name,description)
        self.isSolved = False
    
    def solvePuzzle(self):
        pass
    
    def failPuzzle(self):
        pass
    
    def isPuzzle(self):
        pass


class Challenge():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completion = 0
        self.clues = []
        self.puzzles = []
        self.isCompleted = False
    
    def checkProgress(self):
        pass
    
    def completeChallenge(self):
        pass
    
class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.objects = []
        self.challenges = []
        self.clues = []
    
    def enterRoom(self):
        print(self.description)
        time.sleep(10)
        print("You look around and see:")
        for option in self.objects:
            print(f"- {option.name}: {option.description}")

    def attemptExit(self):
        pass


#room definitions
foyer = Room("Foyer", "To access the castle, there is a huge staircase that branches off to the right and left, with a huge fountain in the center that emerges from the wall. The door is huge and old, and when it opens, using a lot of force, it makes a creaking and frightening noise. Once inside, you can admire a long red carpet, all worn and dirty, which reaches the foot of the stairs. To the left, next to the door, there is a coat rack, and to the right, there is a huge table with a chessboard on it. Behind the table, there is a fireplace that magically lights up once the door is opened. The room is dark, and the only source of light is the fireplace, which illuminates the entire room. In the left corner, you can admire a beautiful antique pendulum clock that hides a secret door that allows access to the library once you guess the right time." )
library = Room("Library", "")
ballroom = Room("Ballroom", "Once inside, all the torches on the walls will magically light up, creating a spooky atmosphere. The grand ballroom leads to a very large room with a grand piano in the center of the dance floor. On either side are tables and chairs covered in cellophane and covered in dust. The room is full of huge windows that allow you to see outside. ")
dungeon = Room("Dungeon", "-The dungeons are located beneath the castle and can be accessed via a secret passage in the piano, which leads directly to the dungeon via a slide. Once inside, visibility is very low, with light coming in through two windows with bars positioned very high up and out of reach. The dungeon is full of cobwebs and dust, and at the back, almost invisible, is a prison with pieces of rock forming a bench. The dungeon is full of covered and dusty objects. On the darkest side of the dungeon is an opening that allows only those who guess the code to open the lock to exit. ")

#challenge definitions

#clue definitions

#puzzle definitions

# main game loop
def gameLoop():
    printTitle()
    name = input("Enter your name: ").lower().replace(" ", "")
    player=(name, 0)
    rooms=[foyer, library, ballroom, dungeon]
    currentRoomindex = 0
    currentRoom = rooms[currentRoomindex]

gameLoop()