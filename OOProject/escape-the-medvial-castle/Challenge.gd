extends CanvasLayer

@onready var prompt_label = $Panel/prompt
@onready var input_field = $Panel/input
@onready var submit_button = $Panel/submit
@onready var close_button = $Panel/close

var current_room: String = ""
var validator_func: Callable = Callable()  # just a stored function reference, NOT a lambda


func _ready() -> void:
	if not submit_button.pressed.is_connected(_on_submit_pressed):
		submit_button.pressed.connect(_on_submit_pressed)

	if not close_button.pressed.is_connected(_on_close_pressed):
		close_button.pressed.connect(_on_close_pressed)

	hide()
	visible = false


func _on_close_pressed() -> void:
	reset_challenge()


func start_challenge(prompt_text: String, room: String, validator: Callable) -> void:
	reset_challenge()

	current_room = room
	validator_func = validator

	prompt_label.text = prompt_text
	input_field.text = ""
	input_field.grab_focus()

	visible = true
	show()


func _on_submit_pressed() -> void:
	var answer: String = input_field.text.strip_edges()  # <-- explicit type fixes the error

	if answer == "":
		prompt_label.text = "Please enter an answer."
		return

	if validator_func != null and validator_func.call(answer):
		Gamestate.solve_puzzle(current_room)
		RoomManager.check_room_completion()   # ⭐ REQUIRED FOR ROOM TRANSITIONS
		reset_challenge()


	else:
		prompt_label.text = "Incorrect. Try again."
		input_field.text = ""
		input_field.grab_focus()


func reset_challenge() -> void:
	hide()
	visible = false
	validator_func = Callable()
	prompt_label.text = ""
	input_field.text = ""
