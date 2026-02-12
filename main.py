# singleton - only one player
class Player:
    def __init__(self, name_Player):
        self.name_Player = name_Player
        self.inv = []
        self.position = None
        self.timeRemaining = 1800   #second
    
    def checkInventory(self):
        print(f"Remaining Time {self.timeRemaining//60} minutes")
        if not self.inv:
            print("the inventory is empty")
        else:
            print("INVENTORY:")
            for item in self.inv:
                print(f"- {item.name}: {item.description}")
    
    def addItemInventory(self,item):
        if item not in self.inv:
            item.pickUp()
            self.inv.append(item)
            print(f"{item.name} added to the inventory")
    
    def modTime(self, minutes):
        self.timeRemaining += minutes * 60
        pass
    
    def restoreTime(self):
        self.timeRemaining = 1800
    

class Object:
    def __init__(self, name_Object, description):
        self.name_Object = name_Object
        self.description_Object = description_Object
    
    def examine(self):
        pass

class Pickup(Object):
    def __init__(self, name_Puzzle, description_Puzzle):
        self.name_Puzzle = name_Puzzle
        self.description_Puzzle = description_Puzzle
        self.isPickedUp = False
        
    def pickUp(self):
        if not self.isPickedUp:
            self.isPickedUp = True
            print(f"{self.name} added to the inventory")
    
    def putBack(self):
        if self.isPickedUp:
            self.isPickedUp = False
        
    
class Clue(Pickup):
    def __init__(self, name_Clue, description_Clue):
        super().__init__(name_Clue, description_Clue)
        self.isInspected = False
    
    def examine(self):
        super().examine()
        self.isInspected = True
    
    def isClue(self):
        pass

class Puzzle(Object):
    def __init__(self, name_Puzzle, description_Puzzle):
        super().__init__(name_Puzzle, description_Puzzle)
        self.isSolved = False
    
    def solvePuzzle(self):
        pass
    
    def failPuzzle(self):
        pass
    
    def isPuzzle(self):
        pass


class Challenge():
    def __init__(self, name_Challenge, description_Challenge):
        self.name_Challenge = name_Challenge
        self.description_Challenge = description_Challenge
        self.completion = 0
        self.clues = []
        self.puzzles = []
        self.isCompleted = False
    
    def checkProgress(self):
        pass
    
    def completeChallenge(self):
        pass
    
class Room():
    def __init__(self, name_Room, description_Room):
        self.name_Room = name_Room
        self.description_Room = description_Room
        self.objects = []
        self.challenges = []
        self.clues = []
    
    def enterRoom(self):
        pass
    def attemptExit(self):
        pass
