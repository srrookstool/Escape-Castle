extends CanvasLayer

var current_room: String = ""
var validator_func: Callable = Callable()

func start_challenge(prompt_text: String, room: String, validator):
	current_room = room
	validator_func = validator

	$prompt.text = prompt_text
	$input.text = ""
	$input.grab_focus()


	visible = true


func _on_submit_pressed():
	var answer = $Panel/input.text.strip_edges()

	# Prevent empty submissions
	if answer == "":
		$Panel/prompt.text = "Please enter an answer."
		return

	# Ensure validator is valid before calling
	if validator_func.is_valid() and validator_func.call(answer):
		visible = false
		Gamestate.solve_puzzle(current_room)
		RoomManager.check_room_completion()

		# Reset validator so old ones don't linger
		validator_func = Callable()
	else:
		$Panel/prompt.text = "Incorrect. Try again."
		$Panel/input.text = ""
		$Panel/input.grab_focus()


func _input(event):
	# Allow pressing Enter to submit
	if visible and event.is_action_pressed("ui_accept"):
		_on_submit_pressed()
