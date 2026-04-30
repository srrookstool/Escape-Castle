extends CanvasLayer
signal challenge_challenge_solved(room_name)

@onready var prompt_label = $Panel/prompt
@onready var input_field = $Panel/input
@onready var submit_button = $Panel/submit
@onready var close_button = $Panel/close

var current_room: String = ""
var validator_func: Callable = Callable()


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
	var answer: String = input_field.text.strip_edges()

	if answer == "":
		prompt_label.text = "Please enter an answer."
		return

	if validator_func != null and validator_func.call(answer):
		print("✔ Correct answer for room:", current_room)

		Gamestate.solve_puzzle(current_room)

		print("✔ EMITTING challenge_challenge_solved for:", current_room)
		emit_signal("challenge_challenge_solved", current_room)

		print("✔ Calling RoomManager.check_room_completion()")
		RoomManager.check_room_completion()

		reset_challenge()
	else:
		Gamestate.modify_time(-60)
		prompt_label.text = "Incorrect. You lost 1 minute. Try again."
		input_field.text = ""
		input_field.grab_focus()


func reset_challenge() -> void:
	hide()
	visible = false
	validator_func = Callable()
	prompt_label.text = ""
	input_field.text = ""
