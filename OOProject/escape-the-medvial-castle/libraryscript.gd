extends Sprite2D

@onready var Challenge = get_node("Challenge")
@onready var Dialogue = get_node("Dialogue")

func _ready():
	Gamestate.current_room_index = 1

	var desc := "The large oak grandfather clock creaks as it opens... " \
	+ "you peek through, combing through spider webs to see walls lined with books and another room with no way out.\n\n" \
	+ "You have now entered the library — it is covered in spider webs, and the only light is through the large window barely covered by fallen drapes.\n\n" \
	+ "The library is filled with old and worn books, some of them so old that they are falling apart. " \
	+ "There is a large wooden desk in the corner of the library, with a drawer slightly open and scattered papers and pens..."

	Dialogue.show_text(desc)
	_init_library_puzzle()


# ---------------------------------------------------------
# INIT
# ---------------------------------------------------------
func _init_library_puzzle():
	Gamestate.book_text = "You see a large wooden desk in the corner of the library, with a drawer that is slightly open. You see scattered papers and pens, but what catches your eye is a framed picture of a %s." % Gamestate.book_clue_word


# ---------------------------------------------------------
# VALIDATOR (NO LAMBDAS)
# ---------------------------------------------------------
func _validate_library(answer: String) -> bool:
	return answer.strip_edges().to_lower() == Gamestate.book_answer.to_lower()


# ---------------------------------------------------------
# START CHALLENGE
# ---------------------------------------------------------
func _start_library_challenge():
	var prompt := "Which book matches the clue?\nEnter the full title:"
	Challenge.start_challenge(prompt, "Library", Callable(self, "_validate_library"))


# ---------------------------------------------------------
# INTERACTION
# ---------------------------------------------------------
func _handle_library_action(letter:String) -> void:
	var room := "Library"
	var required := ["B","R","E","F"]

	match letter:

		"B":
			Dialogue.show_text("You pull out a dusty copy of Romeo and Juliet. A paper falls out with a rose and the quote: 'A rose by any other name...'")
			Gamestate.modify_time(-5)
			Gamestate.mark_examined(room, "B")
			Gamestate.mark_clue_inspected(room, "B")

		"R":
			Dialogue.show_text("You pull out The Great Gatsby. A paper falls out with a clock and the quote: 'So we beat on...'")
			Gamestate.modify_time(-5)
			Gamestate.mark_examined(room, "R")
			Gamestate.mark_clue_inspected(room, "R")

		"E":
			Dialogue.show_text("You pull out Sherlock Holmes. A paper falls out with a dagger and the quote: 'When you have eliminated the impossible...'")
			Gamestate.modify_time(-5)
			Gamestate.mark_examined(room, "E")
			Gamestate.mark_clue_inspected(room, "E")

		"F":
			Dialogue.show_text("You see a large music note barely hanging on the wall. It reads: 'The key to the ballroom is in the music.'")
			Gamestate.modify_time(-5)
			Gamestate.mark_examined(room, "F")
			Gamestate.add_note("Music Notes", "A")

		"D":
			if Gamestate.is_puzzle_solved(room):
				Dialogue.show_text("The desk drawer is already open — you've solved this puzzle.")
				return

			if not Gamestate.all_examined(room, required):
				Dialogue.show_text("You feel like you haven't examined everything yet...")
				return

			if not Challenge.visible:
				Dialogue.show_text(Gamestate.book_text)
				_start_library_challenge()

		_:
			Dialogue.show_text("Nothing happens.")

# BUTTONS — 
func _on_romeoandjuliet_pressed():
	_handle_library_action("B")
	RoomManager.check_room_completion()
func _on_gatsby_pressed():
	_handle_library_action("R")
	RoomManager.check_room_completion()
func _on_sherlock_pressed():
	_handle_library_action("E")
	RoomManager.check_room_completion()
func _on_desk_pressed():
	_handle_library_action("D")
	RoomManager.check_room_completion()
func _on_frame_pressed():
	_handle_library_action("F")
	RoomManager.check_room_completion()
func _on_inventory_pressed():
	$InventoryPanel.refresh_inventory()
	$InventoryPanel.visible = true



# ---------------------------------------------------------
# HOVER ANIMATIONS
# ---------------------------------------------------------
func _on_romeoandjuliet_mouse_entered() -> void:
	$romeoandjuliet/AnimationPlayerR.play("hover_onR")

func _on_romeoandjuliet_mouse_exited() -> void:
	$romeoandjuliet/AnimationPlayerR.play("hover_offR")

func _on_sherlock_mouse_entered() -> void:
	$sherlock/AnimationPlayerS.play("hover_onS")

func _on_sherlock_mouse_exited() -> void:
	$sherlock/AnimationPlayerS.play("hover_offS")

func _on_gatsby_mouse_entered() -> void:
	$gatsby/AnimationPlayerG.play("hover_onG")

func _on_gatsby_mouse_exited() -> void:
	$gatsby/AnimationPlayerG.play("hover_offG")

func _on_desk_mouse_entered() -> void:
	$desk/AnimationPlayerD.play("hover_onD")

func _on_desk_mouse_exited() -> void:
	$desk/AnimationPlayerD.play("hover_offD")

func _on_frame_mouse_entered() -> void:
	$frame/AnimationPlayerF.play("hover_onF")

func _on_frame_mouse_exited() -> void:
	$frame/AnimationPlayerF.play("hover_offF")

func _on_inventory_mouse_entered() -> void:
	$Inventory/GlowInv.play("hover_onI")

func _on_inventory_mouse_exited() -> void:
	$Inventory/GlowInv.play("hover_offI")
