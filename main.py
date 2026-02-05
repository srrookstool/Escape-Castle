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
        pass
    def attemptExit(self):
        pass