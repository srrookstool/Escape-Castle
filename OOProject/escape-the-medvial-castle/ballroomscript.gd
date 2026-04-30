extends Sprite2D

@onready var Challenge = get_node("Challenge")

func _ready():
	Gamestate.current_room_index = 2

	var desc := "As you walk down the spiraling stairs, a golden light begins to appear. " \
	+ "You hear faint classical music echoing through the stone walls.\n\n" \
	+ "You push open a small wooden door and step into the ballroom..."

	$Dialogue.show_text(desc)


# ---------------------------------------------------------
# CHALLENGE
# ---------------------------------------------------------
func _start_ballroom_challenge():
	var prompt := "Enter the correct four‑letter piano sequence:"

	var validator := func(answer:String) -> bool:
		return answer.strip_edges().to_upper() == "CAGE"

	Challenge.start_challenge(prompt, "Ballroom", validator)


# ---------------------------------------------------------
# LOGIC
# ---------------------------------------------------------
func _handle_ballroom_action(letter:String)->void:
	var room := "Ballroom"
	var required := ["F","N"]

	match letter:

		"F":
			var msg := "You see a large music note frame lying on the ground — the notes C and E. " \
			+ "They are the only ones not covered in dust. On the back, an inscription reads: " \
			+ "'The key to the ballroom is in the music.'"

			Gamestate.modify_time(-5)
			Gamestate.mark_examined(room, "F")
			Gamestate.mark_clue_inspected(room, "F")

			# Add music notes
			Gamestate.record_music_note("C")
			Gamestate.record_music_note("E")

			$Dialogue.show_text(msg)

		"N":
			var first_two := Gamestate.door_code.substr(0,2)
			var msg2 := "You find a ripped note on the ground. It reads: %s." % first_two

			Gamestate.modify_time(-5)
			Gamestate.mark_examined(room, "N")
			Gamestate.mark_clue_inspected(room, "N")

			# Add Half Note #2 to inventory
			var digits = Gamestate.door_code.substr(0, 2)
			Gamestate.add_half_note("2", digits)


			$Dialogue.show_text(msg2)

		"P":
			if Gamestate.is_puzzle_solved(room):
				$Dialogue.show_text("The piano lid is already open — you've solved this puzzle.")
				return

			if not Gamestate.all_examined(room, ["F","N"]):
				$Dialogue.show_text("You feel like you haven't examined everything yet...")
				return

			if not Challenge.visible:
				_start_ballroom_challenge()
				return

			# Puzzle solved AFTER correct validator input
			Gamestate.solve_puzzle("Ballroom")
			RoomManager.check_room_completion()

		_:
			$Dialogue.show_text("Nothing happens.")


# ---------------------------------------------------------
# BUTTONS
# ---------------------------------------------------------
func _on_frames_pressed():
	_handle_ballroom_action("F")

func _on_note_pressed():
	_handle_ballroom_action("N")

func _on_piano_pressed():
	_handle_ballroom_action("P")

func _on_inventory_pressed():
	$InventoryPanel.refresh_inventory()
	$InventoryPanel.visible = true


# ---------------------------------------------------------
# HOVER ANIMATIONS 
# ---------------------------------------------------------
func _on_note_mouse_entered() -> void:
	$note/AnimationPlayerN.play("hover_onN")

func _on_note_mouse_exited() -> void:
	$note/AnimationPlayerN.play("hover_offN")

func _on_frames_mouse_entered() -> void:
	$frames/AnimationPlayerF.play("hover_onF")

func _on_frames_mouse_exited() -> void:
	$frames/AnimationPlayerF.play("hover_offF")

func _on_piano_mouse_entered() -> void:
	$piano/AnimationPlayerP.play("hover_onP")

func _on_piano_mouse_exited() -> void:
	$piano/AnimationPlayerP.play("hover_offP")

func _on_inventory_mouse_entered() -> void:
	$Inventory/GlowInv.play("hover_onI")

func _on_inventory_mouse_exited() -> void:
	$Inventory/GlowInv.play("hover_offI")
