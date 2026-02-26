import os
import time
from math import floor, ceil
from random import randint, choice
inventory_button=False
from tqdm import tqdm

# COLOR
AQUA ="#00FFFF"
AZURE = "#069AF3"
BLUE = "#0343DF"
NAVY = "#01153E"

#text wrapper
import textwrap
def wrap(text, width=70):
    return "\n".join(textwrap.wrap(text, width))

#formatting helper
def wrap(text, width=70):
    import textwrap
    return "\n".join(textwrap.wrap(text, width))

def printTitle():
   print("""
░█▀▀░█▀▀░█▀▀░█▀█░█▀█░█▀▀░░░▀█▀░█░█░█▀▀░░░█▄█░█▀▀░█▀▄░▀█▀░█░█░█▀▀░█░█░█▀█░█░░░░░█▀▀░█▀█░█▀▀░▀█▀░█░░░█▀▀
░█▀▀░▀▀█░█░░░█▀█░█▀▀░█▀▀░░░░█░░█▀█░█▀▀░░░█░█░█▀▀░█░█░░█░░▀▄▀░█▀▀░▀▄▀░█▀█░█░░░░░█░░░█▀█░▀▀█░░█░░█░░░█▀▀
░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░░░▀▀▀░░░░▀░░▀░▀░▀▀▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░░▀░░▀▀▀░░▀░░▀░▀░▀▀▀░░░▀▀▀░▀░▀░▀▀▀░░▀░░▀▀▀░▀▀▀
""")

# singleton - only one player
class Player:
    def __init__(self, name, startTime=1800):
        self.name = name
        self.inv = []
        self.position = None
        self.startTime = startTime
        self.timeRemaining = startTime
        # progress bar
        self.pbar = tqdm(total=100, 
                         bar_format='{l_bar}{bar}| {n_fmt}%', 
                         colour=AQUA, 
                         leave=True)

    def updateTotProgress(self, all_rooms):
        total_game_progress = 0
        per_room_weight = 100 / len(all_rooms) #25% each room

        for room in all_rooms:
            # Calc progress bar
            objs_in_room = len(room.objects)
            if objs_in_room > 0:
                inspected = sum(1 for obj in room.objects if obj.examined)
                if room.challenges and room.challenges[0].isCompleted:
                    total_game_progress += per_room_weight
                else:
                    total_game_progress += (inspected / objs_in_room) * per_room_weight
                    break #break if the room is not done

        # color
        if total_game_progress <= 25: self.pbar.colour = AQUA
        elif total_game_progress <= 50: self.pbar.colour = AZURE
        elif total_game_progress <= 75: self.pbar.colour = BLUE
        else: self.pbar.colour = NAVY

        self.pbar.n = int(total_game_progress)
        self.pbar.refresh()
    
    def checkInventory(self):
        print("\n" + "═" * 50)
        print(f"🩸  INVENTORY  🩸".center(50))
        print("═" * 50)

        print(f"⏳  Time Remaining: {self.timeRemaining // 60} minutes and {self.timeRemaining % 60} seconds\n")

        if not self.inv:
            print("Your bag feels cold and empty...")
        else:
            for item in self.inv:
                print(f"• {item.name}")
                print("    " + wrap(item.description, 46))
                print()

        print("═" * 50)
        
    def addItemInventory(self, item):
        if item not in self.inv:
            self.inv.append(item)
            print(f"{item.name} added to the inventory")
    
    
    def modTime(self, seconds):
        self.timeRemaining = floor(self.timeRemaining + seconds)
    
    def restoreTime(self):
        self.timeRemaining = self.startTime

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
    def __init__(self, name, description, contains=None, label=None, interactTime=5, letter=None):
        self.name = name
        self.description = description
        self.label = label if label else name
        self.contains = contains if contains else []
        self.interactTime = interactTime
        self.letter = letter
        self.isOpened = False
        self.isClue = False 
        self.isPuzzle = None 
        self.puzzle = None
        self.triggersChallenge = False
        self.examined = False

        

    def examine(self, player, endInteraction=True):
        print("\n" + wrap(self.description) + "\n")
        self.examined = True
        
        player.modTime(-self.interactTime) # take time away for interacting (default to 5 seconds for all objects)

        # Unlock inventory button when Large Chest is opened
        if self.name.lower() == "large chest":
            global inventory_button
            inventory_button = True
        
        # container handling
        if self.contains:
            self.isOpened = True
            
            print("🕸️  Inside the chest, you find:\n")
            for item in self.contains:
                print(f"  • {item.label}")
            
            # allow user to interact with contents
            interact_attempt = input("\nWhat do you pick..... ").lower().strip()
            interact_success = False
            for item in self.contains:
                if interact_attempt == item.name.lower() or interact_attempt == item.label.lower():
                    interact_success = True
                    item.examine(player)
                    if isinstance(item, Pickup) and item.isPickedUp:
                        self.contains.remove(item)
                        
            
            if interact_attempt and not interact_success:
                print(f"{interact_attempt.capitalize()} is not in {self.name}")

        if endInteraction:
            input("Press enter to continue...")

        # DO NOT start puzzles here
        return self.triggersChallenge

class Pickup(Object):
    def __init__(self, name, description, label=None, interactTime=5, pickupTime=5, letter=None):
        super().__init__(name, description, label=label, interactTime=interactTime, letter=letter)
        self.pickupTime = pickupTime
        
        self.isPickedUp = False
        
    def pickUp(self, player):
        if not self.isPickedUp:
            self.isPickedUp = True
            player.modTime(-self.pickupTime)
            player.addItemInventory(self)
            print(f"{self.name} added to the inventory")

    def examine(self, player):
        super_return = super().examine(player, endInteraction=False) # call inherited examine and delay return
        
        if not self.isPickedUp:
            # give the player the option to take the item
            choice = input(f"Would you like to pick up: {self.name}? (y/n): ").lower()
            if choice == 'y':
                self.pickUp(player)
            else:
                print(f"You leave the {self.name} where it is.")
        else:
            # in inventory, do nothing
            input("Press enter to continue...")    
        
        return super_return            
        
class Clue(Pickup):
    def __init__(self, name, description, label=None, interactTime=5, pickupTime=5, letter=None):
        super().__init__(name, description, label=label, interactTime=interactTime, pickupTime=pickupTime, letter=letter)
        self.isClue = True # lazy way to check object type
        self.isInspected = False
        
    
    def examine(self, player):
        super().examine(player)
        self.isInspected = True
        self.examined = True

class Puzzle(Object):
    def __init__(self,name, description, answer,label=None, interactTime=5, letter=None):
        super().__init__(name, description, label=label, interactTime=interactTime, letter=letter)
        self.answer = answer
        self.isSolved = False

    def examine(self, player):
        if not self.examined:
            super().examine(player, endInteraction=False)

        self.examined = True
        return False
    
    def startPuzzle(self):
        answer = input("Enter your solution: ")
        if answer == self.answer:
            self.isSolved = True
        else:
            print("\nYou entered that wrong.")
        input("Press ENTER to continue...")

    
    def failPuzzle(self):
        pass
    
    def isPuzzle(self):
        pass
    

class Challenge:
    def __init__(self, name, startText, completionText, letter=None):
        self.name = name
        self.startText = startText
        self.completionText = completionText
        self.letter = letter
        self.puzzle = None
        self.isCompleted = False

    def startChallenge(self):
        print("\n" + self.startText)
        input("Press ENTER to begin...")

        if self.puzzle:
            self.puzzle.startPuzzle()

        if self.puzzle and self.puzzle.isSolved:
            self.completeChallenge()

    def completeChallenge(self):
        self.isCompleted = True
        print("\n" + self.completionText)
    
class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.objects = []
        self.challenges = []
    
    def enterRoom(self):
        # Room header
        print("\n" + "─" * 70)
        print(f"🕯️  {self.name.upper()}")
        print("─" * 70 + "\n")

        # Room description
        print(wrap(self.description))

        # Object list
        print("You look around and see:\n")

        for obj in self.objects:
            print(wrap(f"  • {obj.label}"))

        # If any containers were opened earlier, show their revealed items
        for obj in self.objects:
            if obj.contains and obj.isOpened:
                print("\n  👁️  Revealed items:")
                for item in obj.contains:
                    print(f"    → {item.name}")


        print("\n" + "─" * 70)


    def userInteract(self, player, attempt):
        target_obj = None
        for obj in self.objects:
            if (
                attempt.lower() == obj.name.lower()
                or attempt.lower() == obj.label.lower()
                or (obj.letter and attempt.lower() == obj.letter.lower())
            ):
                target_obj = obj
                break

        if not target_obj:
            return False # no valid interaction

        # Examine the object once
        target_obj.examine(player)

        # If this is a puzzle object, we treat it as the challenge trigger
        is_puzzle_trigger = isinstance(target_obj, Puzzle) and target_obj.triggersChallenge

        if is_puzzle_trigger:
            # Only allow challenge if everything has been examined
            if not self.allObjectsExamined():
                print("\nYou feel like you haven't examined everything yet...")
                input("Press ENTER to continue...")
                return target_obj

            # All objects examined → start challenge
            if self.challenges and not self.challenges[0].isCompleted:
                self.challenges[0].startChallenge()

        return target_obj # no valid interaction
    

    def allObjectsExamined(self):
        for obj in self.objects:
            # Clues must be inspected
            if obj.isClue and not obj.isInspected:
                return False

            # Puzzle objects must be examined (but not solved yet)
            if isinstance(obj, Puzzle) and not obj.examined:
                return False

            # Normal objects must be examined
            if not obj.isClue and not isinstance(obj, Puzzle) and not obj.examined:
                return False

        return True
    def attemptExit(self):
        # Must inspect all clues
        for obj in self.objects:
            if obj.isClue and not obj.isInspected:
                return False


        # Must examine all objects
        if not self.allObjectsExamined():
            return False

        # Must complete the challenge

        if self.challenges and not self.challenges[0].isCompleted:
            return False

        return True

# create random parts for puzzles
door_code = f'{randint(0,9999):04}'

# --- CREATE ROOMS ---
foyer = Room("Foyer", "You go to access the castle, there is a huge staircase that branches off to the right and left, with a huge fountain in the center that emerges from the wall. The door is huge and old, and when it opens, using a lot of force, it makes a creaking and frightening noise. Once inside, you admire a long red carpet, all worn and dirty, which reaches the foot of the stairs. To the left, next to the door, there is a coat rack, and to the right, there is a huge table with a chessboard on it. Behind the table, there is a fireplace that magically lights up once the door is opened. The room is dark, and the only source of light is the fireplace, which illuminates the entire room. In the left corner, you can admire a beautiful antique pendulum clock that reads the time of 3:33 AM. ")
library = Room("Library", "The large oak grandfather clock creaks as it opens... you peak through, combing through spider webs to see walls lined with books,and another room with no way out.(insert door sliding old noise)” “You have now entered the library-it is covered in spider webs, and the only light is through the large window barley covered by fallen drapes. You start to look around... ")
ballroom = Room("Ballroom", "... as you are walking down the spiraling stairs, you start to see a golden light appear and the faint sound of.... Classical music? - the stairs led you to a small door with a small looking window, you entered to find the ballroom.")
dungeon = Room("Dungeon", "… once inside, visibility is very low, with light coming in through two windows with bars positioned very high up and out of reach. The dungeon is full of cobwebs and dust, and at the back, almost invisible, is a prison with pieces of rock forming a bench. The dungeon is full of covered and dusty objects. On the darkest side of the dungeon is an opening that allows only those who guess the code to open the lock to exit...")

# --- CREATE OBJECTS ---    
#foyer objects
FCnote1=Clue("A small half ripped note", f"The note reads: {door_code[2:]}.", label="Half Note")
large_chest = Object( "Large Chest", 
                     "You see a large chest on the ground to your right- while brushing away spider webs you notice it looks old and worn,  but it might contain something useful-you open it...",
                     contains=[FCnote1] )
musicnote_G = Object("Broken Frame", "You see a large music note barely hanging on the wall, it is the note G, and it is the only one that is not covered in dust. You examine it, and you notice that there is a small inscription on the back of the note that says 'The key to the ballroom is in the music...")
clockCH=Puzzle("Clock", 
               "You walk up to the clock... it is frozen at midnight. Something feels wrong.", 
               "3:33 am")


#library objects
book1=Clue("A blood-stained, spine-split book (B)",
           "You pull out a dusty copy of Romeo and Juliet, and as you open it, you see a piece of paper fall out- it has an image of a rose on it, and the words 'A rose by any other name would smell as sweet' written on it.", 
           label="A blood-stained, spine-split book (B)",
           letter="B")
book2=Clue("A worm-eaten, leather-bound relic (R)",
           "You pull out a worn copy of The Great Gatsby, and as you open it, a piece of paper falls out- it has an image of a clock on it, and the words 'So we beat on, boats against the current, borne back ceaselessly into the past' written on it.", 
           label="A worm-eaten, leather-bound relic (R)",
           letter="R")
book3=Clue("A skin-bound, iron-nailed grimoire edition (E)",
           "You pull out a tattered copy of Sherlock Holmes, and as you open it, you see a piece of paper fall out- it has an image of a dagger on it, and the words 'When you have eliminated the impossible, whatever remains, however improbable, must be the truth' written on it.",
             label="A skin-bound, iron-nailed grimoire edition (E)",
             letter="E")
desk=Puzzle("A Clutery Desk (D)",
             "You study the framed picture on the desk... it must point to the correct book.",
            "Romeo and Juliet",
            letter="D")
musicnote_A=Object("Inscripted Frame (F)", 
                   "You see a large music note barely hanging on the wall, it is the note A, and it is covered in dust. You examine it, and you notice that there is a small inscription on the back of the note that says 'The key to the ballroom is in the music'.",
                   letter="F")

#Ballroom objects
musicenote_CE=Object("Framed Music Notes", 
                     "You see a large music note barely hanging on the wall, it is the notes C and E, and it is the only one that is not covered in dust. You examine it, and you notice that there is a small inscription on the back of the note that says 'The key to the ballroom is in the music'.")
FCnote2=Object("A small ripped note", 
               f"You see a small ripped note on the ground, badly worn, you pick it up and read the numbers on it- it contains two digits - piece of paper for the final code: {door_code[:2]}.", 
               label= "A small ripped note")
piano=Puzzle("Grand Piano", 
             "You see a grand piano in the corner of the ballroom, it is covered in dust, but it looks like it is still functional. You sit down and start to play the notes you found in the foyer and library, and as you play, you notice that the music starts to change- the top of the paino opens when you play the correct notes, revealing an opening. Enter the notes...", "CAGE")

#Dungeon objects
bench=Object("Bench", 
             "You see a bench made of rock in the corner of the dungeon, you walk over to examine it and you see a multiple carvings of combinations of the same four numbers from the notes all over the bench... what could this mean?")
coveredTable=Clue("Covered Table", 
                  "You see a covered table in the corner of the dungeon, you pull off the cover while coughing from the dust you drag the table tunder  the cellar doors hoping to reach the exit...")#coveredTable must be moved under the cellar doors to reveal the final puzzle
finaldoor=Puzzle("Cellar Doors", 
                 "You uncover a set of cellar doors-hoping they head outside you think about what you have found so far- You try to piece together the clues and figure out the code to open the door. Enter your choices carefully as there may be a consequence... :",
                 "1650")

#Randomized objects
VintageThrone=Object("Vintage Throne", 
                     "You see a large, ornate throne in the center of the dungeon. It is made of dark wood and has intricate carvings. Do you dare to sit down..?")#50/50- sleep potion-lose all time down to 5 minutes, or energizer potion- full restoration of time 
handMirror=Object("Hand Mirror",
                   "You see a small hand mirror on the ground, it is old and cracked, but it still reflects your image. As you look into the mirror, you see a faint image of a ghostly figure behind you. Do you dare to look again..?")#if yes get 5 minute resoration, if no, nothing happens

# --- ADD OBJECTS TO ROOMS ---
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

#CREATE CHALLENGES AND CONNECTION TO PUZZLES,OBJECTS,ROOMS
foyerChallenge = Challenge(
    "Clock Challenge",
    "You walk up to the clock...something feels wrong, and you see that it is stopped at a chilling midnight... put the clock back at the correct time...",
    "A large oak grandfather clock opens at the top of the grand staircase — you enter."
)
foyerChallenge.puzzle = clockCH
foyer.challenges.append(foyerChallenge)
clockCH.triggersChallenge = True

libraryChallenge = Challenge(
    "Book Challenge",
    "You see a large wooden desk in the corner of the library, with a drawer that is slightly open. You see has scattered papers and pens, but what catches your eye is a framed picture of a rose.",
    "The bookcase slides aside, revealing a spiraling staircase downward..."
)
libraryChallenge.puzzle = desk
library.challenges.append(libraryChallenge)
desk.triggersChallenge = True

ballroomChallenge = Challenge(
    "Ballroom Challenge",
    "Golden light fills the room... the piano seems to wait for you.",
    "The piano lid opens — you slide inside and drop into the dungeon."
)
ballroomChallenge.puzzle = piano
ballroom.challenges.append(ballroomChallenge)
piano.triggersChallenge = True


dungeonChallenge = Challenge(
    "Dungeon Challenge",
    "The cellar doors loom above you... only the correct code will open them.",
    "The lock clicks open. The doors swing outward. You escape the castle."
)
dungeonChallenge.puzzle = finaldoor
dungeon.challenges.append(dungeonChallenge)
finaldoor.triggersChallenge = True

#PUZZLE ANSWERS
clockCH.answer = "3:33 am"
desk.answer = "Romeo and Juliet"
piano.answer = "CAGE" #order matters
finaldoor.answer = "1650" #order matters, based on the notes found in the rooms
 
# main game loop
def gameLoop():
    global inventory_button
    printTitle()

    name = input("Enter your name: ").lower().replace(" ", "")
    player = Player(name)


    rooms=[foyer, library, ballroom, dungeon]
    room_index = 0
    current_room = rooms[room_index]
    
    #DEBUG FUNCTIONS, COMMENT OUT WHEN NOT TESTING
    if name == "library":
        room_index = 1
        current_room = library
    elif name == "ballroom":
        room_index = 2
        current_room = ballroom
    elif name == "dungeon":
        room_index = 3
        current_room = dungeon
    
    while True:
        startTurn = time.time()
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # show progress bar
        player.updateTotProgress(rooms)

        current_room.enterRoom()

        # Show inventory button only after chest is opened
        if inventory_button:
            print(f"{'[ Press (i) for Inventory ]':>60}")
        
        user_interact_attempt = input("\nWhat do you pick..... ").lower().strip()

        if user_interact_attempt in ["i", "inv", "inventory"] and inventory_button:
            player.checkInventory()
            input("Press enter to continue...")
            continue
        else:
           valid_room_interaction = current_room.userInteract(player, user_interact_attempt)

        # Unlock inventory button when Large Chest is examined and opened
        if not valid_room_interaction:
                print("Not a valid interaction.")
                input("Press enter to continue...")
                continue

        # --- Logic between interactions --- #

        # Check if the room can be exited
        if current_room.attemptExit():
            if room_index < len(rooms) - 1:
                print(f"\nWith all clues found, you find a way out of the {current_room.name}...")
                room_index += 1
                current_room = rooms[room_index]
                input("Press enter to enter the next room...")
            else:
                if player.checkGameState([]):
                    player.pbar.close()
                    break
            
        
        # Update time and check game state
        turnTime = time.time() - startTurn # 'decision time' on top of interaction time (only happens for valid, non-inventory interactions)
        player.modTime(-turnTime)# Decrease time per interaction
        if player.checkGameState([Challenge("dummy","dummy","dummy")]):
            player.pbar.close()
            break # end the game


gameLoop()
