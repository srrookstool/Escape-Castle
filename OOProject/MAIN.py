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
    def __init__(self, name):
        self.name = name
        self.inv = []
        self.position = None
        self.timeRemaining = 1800
    
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

    def checkGameState(self, challenges):
        # WIN CONDITION:
        if all(ch.isCompleted for ch in challenges):
            print("""░█░█░█▀█░█░█░░░█▀▀░█▀▀░█▀▀░█▀█░█▀█░█▀▀░█▀▄░█
                   \r░░█░░█░█░█░█░░░█▀▀░▀▀█░█░░░█▀█░█▀▀░█▀▀░█░█░▀
                   \r░░▀░░▀▀▀░▀▀▀░░░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░░░▀▀▀░▀▀░░▀""")
            return True

        # LOSE CONDITION: timer ran out
        if self.timeRemaining <= 0:
            print("""░▀█▀░▀█▀░█▄█░█▀▀░█▀▀░░░█░█░█▀█░█░░░█░█░█▀█░█░█░░░█░░░█▀█░█▀▀░█▀▀░█
                   \r░░█░░░█░░█░█░█▀▀░▀▀█░░░█░█░█▀▀░▀░░░░█░░█░█░█░█░░░█░░░█░█░▀▀█░█▀▀░▀
                   \r░░▀░░▀▀▀░▀░▀░▀▀▀░▀▀▀░░░▀▀▀░▀░░░▀░░░░▀░░▀▀▀░▀▀▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀""")
            return True

        # Game continues
        return False

class Object:
    def __init__(self, name, description, contains=None, label=None):
        self.name = name
        self.description = description
        self.label = label if label else name
        self.contains = contains if contains else []
        self.isOpened = False
        self.isClue = False # lazy way to check object type
    
    def examine(self):
        print(self.description)

        # Reveal hidden items only once
        if self.contains and not self.isOpened:
            print("\nInside, you find:")
            for item in self.contains:
                print(f"- {item.name}")
            self.isOpened = True

        elif self.contains and self.isOpened:
            print("\nYou've already opened this.")

        input("Press enter to continue...")

class Pickup(Object):
    def __init__(self, name, description, label=None):
        super().__init__(name, description, label=label)
        self.isPickedUp = False
        
    def pickUp(self):
        if not self.isPickedUp:
            self.isPickedUp = True
            print(f"{self.name} added to the inventory")
    
    def examine(self):
        print(self.description)
        
        if not self.isPickedUp:
            # give the player the option to take the item
            choice = input(f"Would you like to pick up the {self.name}? (y/n): ").lower()
            if choice == 'y':
                self.pickUp()
            else:
                print(f"You leave the {self.name} where it is.")
        else:
            # in inventory, do nothing
            input("Press enter to continue...")                
        
class Clue(Pickup):
    def __init__(self, name, description, label=None):
        super().__init__(name, description, label=label)
        self.isClue = True # lazy way to check object type
        self.isInspected = False
        
    
    def examine(self):
        super().examine()
        self.isInspected = True

class Puzzle(Object):
    def __init__(self,name, description, label=None):
        super().__init__(name, description, label=label)
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
    
    def enterRoom(self):
        print(self.description)
        print()
        print("You look around and see:")
        for option in self.objects:
            if option.label == option.name:
                print(f"[{option.name}]: {option.description}")
            else:
                print(f"[{option.label}] - {option.name}: {option.description}")

        
        for obj in self.objects:
            if obj.contains and obj.isOpened:
                for item in obj.contains:
                    print(f"- {item.name}")
    
    
    def userInteract(self, attempt):
        # Search for the object by name or label
        target_obj = None
        for obj in self.objects:
            if attempt.lower() == obj.name.lower() or attempt.lower() == obj.label.lower():
                target_obj = obj
                break
        
        if target_obj:
            target_obj.examine()
            return target_obj

    
    def attemptExit(self):
        # returns True if all exit conditions are met, False otherwise
        
        # cannot exit if all clues in the room haven't been inspected
        for obj in self.objects:
            if obj.isClue and not obj.isInspected:
                return False


# --- CREATE ROOMS ---
foyer = Room("Foyer", "You go to access the castle, there is a huge staircase that branches off to the right and left, with a huge fountain in the center that emerges from the wall. The door is huge and old, and when it opens, using a lot of force, it makes a creaking and frightening noise. Once inside, you admire a long red carpet, all worn and dirty, which reaches the foot of the stairs. To the left, next to the door, there is a coat rack, and to the right, there is a huge table with a chessboard on it. Behind the table, there is a fireplace that magically lights up once the door is opened. The room is dark, and the only source of light is the fireplace, which illuminates the entire room. In the left corner, you can admire a beautiful antique pendulum clock that reads the time of 3:33 AM. ")
library = Room("Library", "The large oak grandfather clock creaks as it opens... you peak through, combing through spider webs to see walls lined with books,and another room with no way out.(insert door sliding old noise)” “You have now entered the library-it is covered in spider webs, and the only light is through the large window barley covered by fallen drapes. You start to look around... ")
ballroom = Room("Ballroom", "... as you are walking down the spiraling stairs, you start to see a golden light appear and the faint sound of.... Classical music? - the stairs led you to a small door with a small looking window, you entered to find the ballroom.")
dungeon = Room("Dungeon", "… once inside, visibility is very low, with light coming in through two windows with bars positioned very high up and out of reach. The dungeon is full of cobwebs and dust, and at the back, almost invisible, is a prison with pieces of rock forming a bench. The dungeon is full of covered and dusty objects. On the darkest side of the dungeon is an opening that allows only those who guess the code to open the lock to exit...")

# --- CREATE OBJECTS ---    
#foyer objects
FCnote1=Clue("A small half ripped note", "The note reads: 50. Do you take it with you?", label="Half Note")
large_chest = Object( "Large Chest", 
                     "You see a large chest on the ground to your right- it looks old and worn, but it might contain something useful-you open it to find its mainly empty except for half of a ripped small note- it contains two digits - piece of paper for the final code: 50.",
                     contains=[FCnote1] )
musicnote_G = Object("Music Note G", "You see a large music note barely hanging on the wall, it is the note G, and it is the only one that is not covered in dust. You examine it, and you notice that there is a small inscription on the back of the note that says 'The key to the ballroom is in the music'.")
clockCH=Puzzle("Clock", "You walk up to the clock, and you see that it is stopped at a chilling midnight... put the clock back at the correct time.")


#library objects
book1=Clue("Romeo and Juliet","You pull out a dusty copy of Romeo and Juliet, and as you open it,........")
book2=Clue("The Great Gatsby","You pull out a worn copy of The Great Gatsby, and as you open it,........")
book3=Clue("Sherlock Holmes: Study in Scarlett","You pull out a tattered copy of Sherlock Holmes, and as you open it,........")
desk=Object("Desk", "You see a large wooden desk in the corner of the library, with a drawer that is slightly open. You see has scattered papers and pens, but what catches your eye is a framed picture of...”")
musicnote_A=Object("Music Note A", "You see a large music note barely hanging on the wall, it is the note A, and it is covered in dust. You examine it, and you notice that there is a small inscription on the back of the note that says 'The key to the ballroom is in the music'.")

#Ballroom objects
musicenote_CE=Object("Music Note C and E", "You see a large music note barely hanging on the wall, it is the note CE, and it is the only one that is not covered in dust. You examine it, and you notice that there is a small inscription on the back of the note that says 'The key to the ballroom is in the music'.")
FCnote2=Object("A small ripped note", "You see a small ripped note on the ground, badly worn, you pick it up and read the numbers on it- it contains two digits - piece of paper for the final code: 16.", "Half Note")
piano=Puzzle("Grand Piano", "You see a grand piano in the corner of the ballroom, it is covered in dust, but it looks like it is still functional. You sit down and start to play the notes you found in the foyer and library, and as you play, you notice that the music starts to change- the top of the paino opens when you play the correct notes, revealing an opening. Enter the notes...")

#Dungeon objects
bench=Object("Bench", "You see a bench made of rock in the corner of the dungeon, you walk over to examine it and you see a multiple carvings of combinations of the same four numbers from the notes all over the bench... what could this mean?")
coveredTable=Clue("Covered Table", "You see a covered table in the corner of the dungeon, you pull off the cover while coughing from the dust you drag the table tunder  the cellar doors hoping to reach the exit...")#coveredTable must be moved under the cellar doors to reveal the final puzzle
finaldoor=Puzzle("Final Door", "You uncover a set of cellar doors-hoping they head outside you think about what you have found so far- You try to piece together the clues and figure out the code to open the door. Enter your choices carefully as there may be a consequence... :")

#Randomized objects
VintageThrone=Object("Vintage Throne", "You see a large, ornate throne in the center of the dungeon. It is made of dark wood and has intricate carvings. Do you dare to sit down..?")#50/50- sleep potion-lose all time down to 5 minutes, or energizer potion- full restoration of time 
handMirror=Object("Hand Mirror", "You see a small hand mirror on the ground, it is old and cracked, but it still reflects your image. As you look into the mirror, you see a faint image of a ghostly figure behind you. Do you dare to look again..?")#if yes get 5 minute resoration, if no, nothing happens

# --- ADD OBJECTS TO ROOMS ---
foyer.objects.append(FCnote1)
foyer.objects.append(large_chest)
foyer.objects.append(musicnote_G)
foyer.objects.append(clockCH)
library.objects.append(book1)
library.objects.append(book2)
library.objects.append(book3)
library.objects.append(desk)
library.objects.append(musicnote_A)
ballroom.objects.append(musicenote_CE)
ballroom.objects.append(piano)
ballroom.objects.append(FCnote2)
dungeon.objects.append(bench)
dungeon.objects.append(coveredTable)
dungeon.objects.append(finaldoor)      


# main game loop
def gameLoop():
    printTitle()

    name = input("Enter your name: ").lower().replace(" ", "")
    player = Player(name)

    rooms=[foyer, library, ballroom, dungeon]
    room_index = 0
    current_room = rooms[room_index]
    
    while True:
        current_room.enterRoom()
        
        user_interact_attempt = input("\nWhat would you like to interact with? ").lower().strip()
        
        interacted = current_room.userInteract(user_interact_attempt)
        
        
        if interacted:
            if isinstance(interacted, Pickup) and not interacted.isPickedUp:
                player.addItemInventory(interacted)
        else:
            print("Not a valid interaction.")
            input("Press enter to continue...")

        os.system('cls' if os.name == 'nt' else 'clear')
        
        # --- Logic between interactions --- #
        
        # Check if the room can be exited
        if current_room.attemptExit():
            # If there are more rooms, move to the next one
            if room_index < len(rooms) - 1:
                print(f"\nWith all clues found, you find a way out of the {current_room.name}...")
                room_index += 1
                current_room = rooms[room_index]
                input("Press enter to enter the next room...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                # Final room logic or win condition check
                if player.checkGameState([]): # TODO: Pass challenges when if implemented
                    break
        
        # Update time and check game state
        player.modTime(-1) # Decrease time per interaction
        if player.checkGameState([Challenge("dummy","dummy")]):
            break
    
gameLoop()
