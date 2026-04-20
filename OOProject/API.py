from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# -------------------------
# Data Models
# -------------------------

class ActionRequest(BaseModel):
    player_name: str
    action: str   # like "F", "L", "C", etc.

# -------------------------
# Fake Game Logic (Replace later)
# -------------------------

# This is where you map your Godot button IDs to descriptions
OBJECT_RESPONSES = {
    "F": "You see a large music note frame. The inscription reads: 'The key to the ballroom is in the music...'",
    "L": "You open the large chest. Inside you find a small ripped note...",
    "C": "You walk up to the clock. Something feels wrong... Put the clock back at the correct time.",
    "B": "You examine the bench. Strange carvings cover the stone surface...",
    "P": "You sit at the piano. The keys feel cold... maybe the notes you found will help.",
    "N": "You pick up the small ripped note. It contains part of a code...",
}

# -------------------------
# API ROUTES
# -------------------------

@app.get("/")
def home():
    return {"message": "Escape Castle API is running!"}


@app.post("/action")
def handle_action(request: ActionRequest):
    """
    Godot sends:
    {
        "player_name": "hannah",
        "action": "F"
    }
    """

    action = request.action.upper()

    # Look up the response text
    if action in OBJECT_RESPONSES:
        description = OBJECT_RESPONSES[action]
    else:
        description = "Nothing happens. That object doesn't seem interactive."

    # Return JSON for Godot to display
    return {
        "player": request.player_name,
        "message": description,
        "inventory": [],          # you can fill this later
        "time_remaining": 1800,   # update later with real logic
        "action_required": None   # or "solve_puzzle", "choose_item", etc.
    }
