extends Node

var _is_changing := false

func _ready():
    _is_changing = false


# ---------------------------------------------------------
# MAIN ROOM CHECKER
# ---------------------------------------------------------
func check_room_completion():
    var i := Gamestate.current_room_index
    print("Checking room:", i)

    # FOYER → LIBRARY
    if i == 0 and Gamestate.is_puzzle_solved("Foyer"):
        print("Going to Library")
        Gamestate.current_room_index = 1
        _change_room("res://library.tscn")
        return

    # LIBRARY → BALLROOM
    if i == 1 and Gamestate.is_puzzle_solved("Library"):
        print("Going to Ballroom")
        Gamestate.current_room_index = 2
        _change_room("res://ballroom.tscn")
        return

    # BALLROOM → FINAL ROOM
    if i == 2 and Gamestate.is_puzzle_solved("Ballroom"):
        print("Going to Final Room")
        Gamestate.current_room_index = 3
        _change_room("res://finalroom.tscn")
        return

    # DUNGEON → ESCAPED
    if i == 3 and Gamestate.is_puzzle_solved("Dungeon"):
        print("Escaped!")
        Gamestate.current_room_index = 4
        _change_room("res://escapedscene.tscn")
        return


# ---------------------------------------------------------
# INTERNAL ROOM LOADER
# ---------------------------------------------------------
func _change_room(path: String):
    if _is_changing:
        print("Already changing rooms, skipping")
        return

    _is_changing = true

    print("Changing to:", path)
    get_tree().change_scene_to_file(path)
