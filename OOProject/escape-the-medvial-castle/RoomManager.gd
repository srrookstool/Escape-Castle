extends Node

var _is_changing := false

func check_room_completion():
    var i := Gamestate.current_room_index

    # FOYER → LIBRARY
    if i == 0 and Gamestate.is_puzzle_solved("Foyer"):
        _change_room("res://Library.tscn")
        return

    # LIBRARY → BALLROOM
    if i == 1 and Gamestate.is_puzzle_solved("Library"):
        _change_room("res://Ballroom.tscn")
        return

    # BALLROOM → FINAL ROOM
    if i == 2 and Gamestate.is_puzzle_solved("Ballroom"):
        _change_room("res://finalroom.tscn")
        return

    # DUNGEON → ESCAPED
    if i == 3 and Gamestate.is_puzzle_solved("Dungeon"):
        _change_room("res://escapedscene.tscn")
        return


func _change_room(path: String):
    if _is_changing:
        return

    _is_changing = true
    get_tree().change_scene_to_file(path)
