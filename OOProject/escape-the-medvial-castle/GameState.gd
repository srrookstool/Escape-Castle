extends Node
class_name GameState

# ---------------------------------------------------------
# PLAYER DATA
# ---------------------------------------------------------
var player_name: String = ""
var inventory: Array[String] = []
var notes := {}

var start_time := 1800
var time_remaining := 1800

# ---------------------------------------------------------
# ROOM PROGRESSION
# ---------------------------------------------------------
var rooms := ["Foyer", "Library", "Ballroom", "Dungeon"]
var current_room_index := 0

var room_solved := [false, false, false, false]
var can_move_back := true

# ---------------------------------------------------------
# RANDOMIZED PUZZLE ANSWERS
# ---------------------------------------------------------
var clock_time := ""
var door_code := ""
var book_answer := ""
var book_clue_word := ""
var piano_answer := "CAGE"

# ---------------------------------------------------------
# OBJECT STATE TRACKING
# ---------------------------------------------------------
var examined_objects := {}
var inspected_clues := {}

var puzzle_solved := {
	"Foyer": false,
	"Library": false,
	"Ballroom": false,
	"Dungeon": false
}

# ---------------------------------------------------------
# SPECIAL INTERACT RANDOMIZATION
# ---------------------------------------------------------
var throne_effect := ""
var mirror_effect := ""

# ---------------------------------------------------------
# INITIALIZATION
# ---------------------------------------------------------
func _ready():
	randomize()
	_generate_random_values()
	_reset_object_tracking()

func _generate_random_values():
	var hour = randi_range(1, 12)
	var minute = randi_range(0, 59)
	var ampm = "AM" if (hour == 12 or hour < 8) else "PM"
	clock_time = "%d:%02d %s" % [hour, minute, ampm]

	door_code = "%04d" % randi_range(0, 9999)

	var options = [
		["Romeo and Juliet", "rose"],
		["The Great Gatsby", "clock"],
		["Sherlock Holmes", "dagger"]
	]
	var pick = options[randi() % options.size()]
	book_answer = pick[0]
	book_clue_word = pick[1]

	if randf() < 0.3:
		throne_effect = "restore" if randf() < 0.5 else "lose"
	else:
		throne_effect = "none"

	mirror_effect = "add_time" if randf() < 0.3 else "none"

func _reset_object_tracking():
	for room in rooms:
		examined_objects[room] = {}
		inspected_clues[room] = {}

# ---------------------------------------------------------
# PLAYER FUNCTIONS
# ---------------------------------------------------------
func set_player_name(name: String):
	player_name = name

func add_inventory(item: String):
	if item not in inventory:
		inventory.append(item)

func add_note(category: String, entry):
	if not notes.has(category):
		notes[category] = []
	notes[category].append(entry)

func modify_time(seconds: int):
	time_remaining += seconds
	if time_remaining < 0:
		time_remaining = 0

func restore_time():
	time_remaining = start_time

# ---------------------------------------------------------
# ROOM FUNCTIONS
# ---------------------------------------------------------
func get_current_room() -> String:
	return rooms[current_room_index]

func move_forward():
	if current_room_index < rooms.size() - 1:
		room_solved[current_room_index] = true
		current_room_index += 1

func move_back():
	if current_room_index > 0 and can_move_back:
		current_room_index -= 1

# ---------------------------------------------------------
# OBJECT STATE FUNCTIONS
# ---------------------------------------------------------
func mark_examined(room: String, letter: String):
	examined_objects[room][letter] = true

func mark_clue_inspected(room: String, letter: String):
	inspected_clues[room][letter] = true

func is_examined(room: String, letter: String) -> bool:
	return examined_objects[room].get(letter, false)

func is_clue_inspected(room: String, letter: String) -> bool:
	return inspected_clues[room].get(letter, false)

func all_examined(room: String, letters: Array) -> bool:
	for letter in letters:
		if not is_examined(room, letter):
			return false
	return true

func all_clues_inspected(room: String, letters: Array) -> bool:
	for letter in letters:
		if not is_clue_inspected(room, letter):
			return false
	return true

# ---------------------------------------------------------
# CHALLENGE START LOGIC (NEW)
# ---------------------------------------------------------
func should_start_challenge(room: String, required_letters: Array) -> bool:
	# Challenge starts ONLY when:
	# 1. All required objects are examined
	# 2. Puzzle is NOT already solved
	return all_examined(room, required_letters) and not is_puzzle_solved(room)

# ---------------------------------------------------------
# PUZZLE FUNCTIONS
# ---------------------------------------------------------
func solve_puzzle(room: String):
	puzzle_solved[room] = true

func is_puzzle_solved(room: String) -> bool:
	return puzzle_solved[room]

# ---------------------------------------------------------
# GAME STATE CHECK
# ---------------------------------------------------------
func is_game_won() -> bool:
	for room in rooms:
		if not puzzle_solved[room]:
			return false
	return true

func is_game_lost() -> bool:
	return time_remaining <= 0
