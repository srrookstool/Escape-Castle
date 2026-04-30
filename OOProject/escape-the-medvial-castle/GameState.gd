extends Node

# ------------------------------
# PLAYER DATA
# ------------------------------
var player_name: String = ""
var inventory: Array[String] = []
var notes := {}

# ------------------------------
# TIME SYSTEM
# ------------------------------
var start_time := 1800
var time_remaining := 1800

# ------------------------------
# ROOM SYSTEM (SINGLE SOURCE OF TRUTH)
# ------------------------------
var rooms := ["Foyer", "Library", "Ballroom", "Dungeon"]
var current_room_index := 0

# ------------------------------
# PUZZLE STATE (ONLY SYSTEM USED)
# ------------------------------
var puzzle_solved := {
	"Foyer": false,
	"Library": false,
	"Ballroom": false,
	"Dungeon": false
}

# ------------------------------
# EXAMINATION TRACKING
# ------------------------------
var examined_objects := {}
var inspected_clues := {}

# ------------------------------
# RANDOMIZED PUZZLE VALUES
# ------------------------------
var clock_time := ""
var door_code := ""

var book_answer : String = ""
var book_clue_word := ""
var book_text := ""

var piano_answer := "CAGE"

var throne_effect := ""
var mirror_effect := ""

# ------------------------------
# READY
# ------------------------------
func _ready():
	randomize()
	_generate_random_values()
	_reset_object_tracking()


# ------------------------------
# RANDOM GENERATION
# ------------------------------
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

	throne_effect = "restore" if randf() < 0.5 else "lose"
	mirror_effect = "add_time" if randf() < 0.3 else "none"


# ------------------------------
# RESET TRACKING
# ------------------------------
func _reset_object_tracking():
	for room in rooms:
		examined_objects[room] = {}
		inspected_clues[room] = {}


# ------------------------------
# PLAYER DATA HELPERS
# ------------------------------
func set_player_name(name: String):
	player_name = name

func add_inventory(item: String):
	if item not in inventory:
		inventory.append(item)

func add_note(category: String, entry):
	if not notes.has(category):
		notes[category] = []
	notes[category].append(entry)


# ------------------------------
# TIME SYSTEM
# ------------------------------
func modify_time(seconds: int):
	time_remaining += seconds
	if time_remaining < 0:
		time_remaining = 0

func restore_time():
	time_remaining = start_time


# ------------------------------
# ROOM SYSTEM (CLEAN VERSION)
# ------------------------------
func get_current_room() -> String:
	return rooms[current_room_index]


# ONLY RoomManager should call this
func advance_room():
	if current_room_index < rooms.size() - 1:
		current_room_index += 1
		print("Room advanced to:", get_current_room())


# ------------------------------
# PUZZLE SYSTEM (FIXED)
# ------------------------------
func solve_puzzle(room: String):
	puzzle_solved[room] = true
	print("✔ Puzzle solved:", room)


func is_puzzle_solved(room: String) -> bool:
	var result = puzzle_solved.get(room, false)
	print("Checking puzzle state:", room, "=", result)
	return result


func is_game_won() -> bool:
	for room in rooms:
		if not puzzle_solved.get(room, false):
			return false
	return true


func is_game_lost() -> bool:
	return time_remaining <= 0


# ------------------------------
# EXAMINATION LOGIC
# ------------------------------
func mark_examined(room: String, letter: String):
	if not examined_objects.has(room):
		examined_objects[room] = {}
	examined_objects[room][letter] = true


func mark_clue_inspected(room: String, letter: String):
	if not inspected_clues.has(room):
		inspected_clues[room] = {}
	inspected_clues[room][letter] = true


func is_examined(room: String, letter: String) -> bool:
	return examined_objects.get(room, {}).get(letter, false)


func all_examined(room: String, letters: Array) -> bool:
	var room_dict = examined_objects.get(room, {})
	for letter in letters:
		if not room_dict.get(letter, false):
			return false
	return true


func should_start_challenge(room: String, required_letters: Array) -> bool:
	return all_examined(room, required_letters) and not is_puzzle_solved(room)
# ------------------------------
# SPECIAL GAME LOGIC HELPERS
# ------------------------------

func record_clock_time():
	add_note("Clock Time", clock_time)

func record_music_note(note: String):
	add_note("Music Notes", note)

func add_book_to_inventory(title: String):
	add_inventory(title)

func add_half_note(id: String, digits: String):
	var desc = "A half note containing the digits: %s" % digits
	add_inventory(desc)
