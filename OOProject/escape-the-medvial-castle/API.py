from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# ---------------------------------------------------------
# PUZZLE VARIABLES
# ---------------------------------------------------------

clock_hour = random.randint(1, 12)
clock_time = f"{clock_hour}:{random.randint(0,59):02} " + ("AM" if clock_hour < 8 or clock_hour == 12 else "PM")

door_code = f"{random.randint(0,9999):04}"

book_answer, book_clue = random.choice([
    ("Romeo and Juliet", "rose"),
    ("The Great Gatsby", "clock"),
    ("Sherlock Holmes", "dagger")
])

book_challenge_text = (
    f"You see a large wooden desk in the corner of the library. "
    f"A framed picture of a {book_clue} sits on top."
)

# ---------------------------------------------------------
# REQUEST MODEL
# ---------------------------------------------------------

class ActionRequest(BaseModel):
    room: str
    action: str

# ---------------------------------------------------------
# ROOM + LETTER + DESCRIPTION
# ---------------------------------------------------------

RESPONSES = {

    # -------------------- FOYER --------------------
    "Foyer": {
        "L": "You see a large chest on the ground to your right. It looks old and worn, but it might contain something useful—you open it...",
        "N": f"The note reads the last two digits of the final code: {door_code[2:]}.",
        "F": "You see a large music note barely hanging on the wall. On the back, an inscription reads: 'The key to the ballroom is in the music...'",
        "C": f"You walk up to the clock... it is frozen at midnight. Something feels wrong. The correct time must be: {clock_time}."
    },

    # -------------------- LIBRARY --------------------
    "Library": {
        "B": "Romeo and Juliet — a rose clue falls out.",
        "R": "The Great Gatsby — a clock clue falls out.",
        "E": "Sherlock Holmes — a dagger clue falls out.",
        "D": book_challenge_text,
        "F": "A dusty music note frame with the letter A. Another inscription reads: 'The key to the ballroom is in the music.'"
    },

    # -------------------- BALLROOM --------------------
    "Ballroom": {
        "F": "Framed notes C and E hang on the wall. Another inscription reads: 'The key to the ballroom is in the music.'",
        "P": "You sit at the grand piano. As you play the notes you found, the music begins to change...",
        "N": f"You find a small ripped note. It contains the first two digits of the final code: {door_code[:2]}."
    },

    # -------------------- DUNGEON --------------------
    "Dungeon": {
        "B": "A stone bench covered in carved numbers... they match the clues you've found.",
        "T": "You pull the cover off the table and drag it under the cellar doors...",
        "D": f"You uncover the cellar doors. You try to piece together the clues and enter the final code: {door_code}."
    },

    # -------------------- RANDOM OBJECTS --------------------
    "Random": {
        "V": "You see a large vintage throne. Do you dare to sit down?",
        "M": "You see a cracked hand mirror. Behind your reflection, a ghostly figure appears... do you dare to look again?"
    }
}

# ---------------------------------------------------------
# API ENDPOINT
# ---------------------------------------------------------

@app.post("/action")
def handle_action(request: ActionRequest):
    room = request.room
    action = request.action.upper()

    description = RESPONSES.get(room, {}).get(
        action,
        "Nothing happens. That object doesn't seem interactive."
    )

    return {
        "message": description,
        "inventory": [],
        "time_remaining": 1800,
        "action_required": None
    }
