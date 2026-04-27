extends Node

func check_room_completion():
    var room := Gamestate.get_current_room()

    match room:

        "Foyer":
            if Gamestate.is_puzzle_solved("Foyer"):
                get_tree().change_scene_to_file("res://Library.tscn")

        "Library":
            if Gamestate.is_puzzle_solved("Library"):
                get_tree().change_scene_to_file("res://Ballroom.tscn")

        "Ballroom":
            if Gamestate.is_puzzle_solved("Ballroom"):
                get_tree().change_scene_to_file("res://Dungeon.tscn")

        "Dungeon":
            if Gamestate.is_puzzle_solved("Dungeon"):
                get_tree().change_scene_to_file("res://WinScreen.tscn")
