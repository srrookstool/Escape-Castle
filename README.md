# Escape from the Medieval Castle
A fully text‑based virtual escape room built using object‑oriented programming principles.  
Players explore four rooms, uncover clues, solve puzzles, manage time, and attempt to escape before the clock runs out.

Created by:  
**Hannah Dees, Samuel Rookstool, Sara Cogoli, Devean Cordes**  
Course: **CS 3700**

---

## Game Overview
The player enters an old medieval castle while searching for missing friends.  
The door locks behind them, and they must solve **four room‑based challenges** before time expires.  
If the player succeeds, they escape. If not, they join the missing friends in the dungeon.

**Core gameplay loop:**
1. Enter a room  
2. Inspect objects  
3. Collect clues  
4. Solve puzzles  
5. Unlock the next room  
6. Escape before time runs out  

---

## Key Mechanics
- **Timer:** 30–60 minutes  
- **Time penalties:** Wrong puzzle guesses  
- **Time bonuses:** Randomized hidden items  
- **4 rooms:** Foyer → Library → Grand Ballroom → Dungeon  
- **3 clues per room**  
- **Music‑note mini‑challenge in every room**  
- **Final code solution:** 1650  
- **Inventory system:** Player can view items at any time  
- **Locked doors:** Play sound until all clues/puzzles are completed  
- **Room progression:** Player can only backtrack starting in Room 3  

---

## Object‑Oriented Architecture

### **PLAYER**
**Attributes**
- Name  
- Position  
- Inventory (Object[])  
- TimeRemaining  

**Actions**
- checkInventory()  
- addItemInventory()  
- loseTime()  
- gainTime()  
- restoreTime()  

---

### **OBJECT (Base Class)**
**Attributes**
- Name  
- Description  
- isPickedUp  

**Actions**
- examineObject()  
- pickUp()  
- putBack()  

---

### **CLUE (inherits OBJECT)**
**Attributes**
- isInspected  

**Actions**
- examineClue()  
- isClue()  

*Inspecting a clue counts toward challenge completion.*

---

### **PUZZLE (inherits CLUE → OBJECT)**
**Attributes**
- isSolved  

**Actions**
- solvePuzzle()  
- failPuzzle() → player.loseTime(1)  
- isPuzzle()  

**Examples**
- Clock puzzle  
- Music note puzzle (C‑A‑G‑E)  
- Final lock (1650)  

---

### **CHALLENGE**
**Attributes**
- Name  
- Description  
- Completion count  
- Clues[]  
- Puzzles[]  
- isCompleted  

**Actions**
- checkProgress()  
- completeChallenge() → unlocks door + plays sound  

---

### **ROOM**
**Attributes**
- Name  
- Description  
- Challenge[]  
- Clues[]  
- Objects[]  

**Actions**
- enterRoom()  
- attemptExit() (locked until challenge completed)  

---

## Room Descriptions & Challenges

---

# **1. Foyer**
**Description:**  
A grand staircase, fountain, fireplace, chess table, and a hidden pendulum clock puzzle.  
The only light comes from the magically lit fireplace.

**Clues & Objects**
- Large chest → contains half‑ripped note (“50”)  
- Music note picture: **G**  
- Grandfather clock puzzle  

**Challenge:**  
Guess the correct time on the clock.  
Once solved, the grandfather clock opens to reveal the Library.

---

# **2. Library**
**Description:**  
A dusty, dim room filled with old books, a desk, and a music note picture.

**Clues & Objects**
- Bookcase → contains a hint (kept in inventory)  
- Desk → contains a framed picture clue  
- Music note picture: **A**  

**Challenge:**  
Identify the correct book based on the desk clue.  
Once solved, the bookcase slides open to reveal a spiraling staircase.

---

# **3. Grand Ballroom**
**Description:**  
Torches ignite automatically. A grand piano sits in the center.  
Dusty tables and massive windows create a haunting atmosphere.

**Clues & Objects**
- Two dusty miniature paintings → reveal notes **C** and **E**  
- Grand piano  
- Half‑ripped note (“16”)  

**Challenge:**  
A music‑note memory puzzle.  
The player must recall the notes from previous rooms and enter them in order.  
**Solution:** C‑A‑G‑E  

Once solved, the piano tail opens and the player slides into the Dungeon.

---

# **4. Dungeon**
**Description:**  
Low visibility, barred windows, cobwebs, and a final locked exit.

**Clues & Objects**
- Prison bench  
- Covered object → reveals item needed to reach final door  
- Final door code: **1650**  

**Randomized Objects**
- **Hand mirror:** +5 minutes  
- **Vintage throne:** 50/50 chance  
  - Sleep potion → reduce time to 5 minutes  
  - Energizer potion → full time restoration  

**Challenge:**  
Enter the correct final code using the notes found throughout the castle.  
Once solved, the ending screen scrolls line‑by‑line like a story reveal.

---

## Win/Lose Conditions
**Win:**  
Solve all four room challenges and escape before time expires.

**Lose:**  
Timer reaches zero → player is captured and joins the missing friends.

Both endings allow the player to restart or exit.

---

## Features Implemented
- Full OOP class hierarchy  
- Room‑based progression  
- Inventory system  
- Time management system  
- Randomized bonus items  
- Multiple puzzle types  
- Sound cues for locked/unlocked doors  
- Narrative‑driven text interactions  

---
