# singleton - only one player
class Player:
    def __init__(self, name_Player):
        self.name_Player = name_Player
        self.inv = []
        self.position = None
        self.timeRemaining = 1800
    
    @property
    def minTime(self):
        minutes, seconds = divmod(self.timeRemaining, 60)
        return f'{minutes}:{seconds}'
    
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
    def __init__(self, name_Object, description):
        self.name_Object = name_Object
        self.description_Object = description_Object
    
    def examine(self):
        pass

class Pickup(Object):
    def __init__(self, name_Pick, description_Pick):
        super().__init__(name_Pick, description_Pick)
        self.isPickedUp = False
        
    def pickUp(self):
        pass
    
    def putBack(self):
        pass
        
    
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
