extends Sprite2D

func _ready():
    Gamestate.current_room_index = 2

    var desc := "As you walk down the spiraling stairs, a golden light begins to appear. " \
    + "You hear faint classical music echoing through the stone walls.\n\n" \
    + "You push open a small wooden door and step into the ballroom..."

    $Dialogue.show_text(desc)


# ------------------ CHALLENGE ------------------
func _start_ballroom_challenge():
    var prompt := "Enter the correct four‑letter piano sequence:"
    Challenge.start_challenge(prompt, "Ballroom", _validate_ballroom)

func _validate_ballroom(answer:String)->bool:
    return answer.to_upper() == "CAGE"


# ------------------ LOGIC ------------------
func _handle_ballroom_action(letter:String)->void:
    var room := "Ballroom"

    match letter:

        "F":
            var msg := "You see a framed set of music notes — C and E — barely hanging on the wall."

            Gamestate.modify_time(-5)
            Gamestate.mark_examined(room, "F")
            Gamestate.mark_clue_inspected(room, "F")
            Gamestate.add_note("Music Notes", "C")
            Gamestate.add_note("Music Notes", "E")
            $Dialogue.show_text(msg)


        "N":
            var first_two := Gamestate.door_code.substr(0,2)
            var msg2 := "You find a ripped note on the ground. It reads: %s." % first_two

            Gamestate.modify_time(-5)
            Gamestate.mark_examined(room, "N")
            Gamestate.mark_clue_inspected(room, "N")
            $Dialogue.show_text(msg2)


        "P":
            if Gamestate.all_examined(room, ["F","N"]):
                _start_ballroom_challenge()
            else:
                $Dialogue.show_text("You feel like you haven't examined everything yet...")


        _:
            $Dialogue.show_text("Nothing happens.")


# ------------------ BUTTONS ------------------
func _on_frames_pressed():
    _handle_ballroom_action("F")
    RoomManager.check_room_completion()

func _on_note_pressed():
    _handle_ballroom_action("N")
    RoomManager.check_room_completion()

func _on_piano_pressed():
    _handle_ballroom_action("P")
    RoomManager.check_room_completion()

func _on_InventoryButton_pressed():
    $InventoryPanel.refresh_inventory()
    $InventoryPanel.visible = true

# ---------------------------------------------------------------
# HOVER ANIMATIONS
# ---------------------------------------------------------------
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
