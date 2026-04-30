extends Sprite2D
@onready var Challenge = get_node("Challenge")

func _ready():
	Gamestate.current_room_index = 0

	$glowL.modulate = Color(1,1,1,0)
	$glowF.modulate = Color(1,1,1,0)
	$glowC.modulate = Color(1,1,1,0)

	var desc := "Looking around... you find a way to access the castle, " \
	+ "there is a huge staircase that branches off to the right and left, with a huge fountain in the center that emerges from the wall. " \
	+ "The door is huge and old, and when it opens, using a lot of force, it makes a creaking and frightening noise. " \
	+ "Once inside, you admire a long red carpet, all worn and dirty, which reaches the foot of the stairs. " \
	+ "To the left, next to the door, there is a coat rack, and to the right, there is a huge table with a chessboard on it. " \
	+ "Behind the table, there is a fireplace that magically lights up once the door is opened. " \
	+ "The room is dark, and the only source of light is the fireplace, which illuminates the entire room. " \
	+ "In the left corner, you can admire a beautiful antique pendulum clock that reads the time of %s.\n\n" % Gamestate.clock_time

	$Dialogue.show_text(desc)


# ---------------------------------------------------------
# CHALLENGE LOGIC 
# ---------------------------------------------------------
func _start_foyer_challenge():
	var prompt := "Enter the correct time shown on the pendulum clock:"
	var validator := func(answer:String) -> bool: return answer.strip_edges().to_upper().replace(" ", "") in [Gamestate.clock_time.to_upper().replace(" ", ""), Gamestate.clock_time.split(" ")[0].to_upper().replace(" ", "")]
	Challenge.start_challenge(prompt, "Foyer", validator)



# ---------------------------------------------------------
# ROOM INTERACTION LOGIC
# ---------------------------------------------------------
func _handle_foyer_action(action:String)->void:
	var room := "Foyer"

	match action:

		"B":
			Gamestate.modify_time(-5)
			Gamestate.mark_examined(room, "B")
			$Dialogue.show_text("You see a large music note barely hanging on the wall. " \
			+ "It is the note G, and it is the only one not covered in dust. " \
			+ "On the back, an inscription reads: 'The key to the ballroom is in the music.'")

		"L":
			var msg := "You see a large chest on the ground to your right— " \
			+ "while brushing away spider webs you notice it looks old and worn... " \
			+ "Inside the chest, you find a small ripped note.\n" \
			+ "The note reads the last two digits of the final code: %s." \
			% Gamestate.door_code.substr(2,2)

			if "Half Note" not in Gamestate.inventory:
				Gamestate.inventory.append("Half Note")

			Gamestate.modify_time(-5)
			Gamestate.mark_examined(room, "L")
			Gamestate.mark_clue_inspected(room, "L")
			$Dialogue.show_text(msg)

		"C":
			Gamestate.modify_time(-5)
			Gamestate.mark_examined(room, "C")
			$Dialogue.show_text("You examine the antique pendulum clock closely...")

		_:
			$Dialogue.show_text("Nothing happens.")


# ---------------------------------------------------------
# BUTTONS
# ---------------------------------------------------------
func _on_brokenframe_pressed() -> void:
	_handle_foyer_action("B")
	RoomManager.check_room_completion()

func _on_large_chest_pressed() -> void:
	_handle_foyer_action("L")
	RoomManager.check_room_completion()

func _on_clock_pressed() -> void:
	var room := "Foyer"
	var required := ["B","L"]

	if Gamestate.is_puzzle_solved(room):
		$Dialogue.show_text("The clock is already set correctly.")
		return

	if not Gamestate.all_examined(room, required):
		$Dialogue.show_text("You feel like you haven't examined everything yet...")
		return

	if not Challenge.visible:
		_start_foyer_challenge()

	RoomManager.check_room_completion()


func _on_inventory_pressed() -> void:
	$InventoryPanel.refresh_inventory()
	$InventoryPanel.visible = true


# ---------------------------------------------------------
# HOVER ANIMATIONS
# ---------------------------------------------------------
func _on_brokenframe_mouse_entered() -> void:
	$brokenframe/GlowAnimatorF.play("hover_on")

func _on_brokenframe_mouse_exited() -> void:
	$brokenframe/GlowAnimatorF.play("hover_off")

func _on_large_chest_mouse_entered() -> void:
	$"large_chest"/GlowAnimatorL.play("hover_onC")

func _on_large_chest_mouse_exited() -> void:
	$"large_chest"/GlowAnimatorL.play("hover_offC")

func _on_clock_mouse_entered() -> void:
	$clock/GlowAnimatorC.play("hover_onL")

func _on_clock_mouse_exited() -> void:
	$clock/GlowAnimatorC.play("hover_offL")

func _on_inventory_mouse_entered() -> void:
	$Inventory/GlowInv.play("hover_onI")

func _on_inventory_mouse_exited() -> void:
	$Inventory/GlowInv.play("hover_offI")
