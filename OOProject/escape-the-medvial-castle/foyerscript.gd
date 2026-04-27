extends Sprite2D

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


# ------------------ CHALLENGE ------------------
func _start_foyer_challenge():
    var prompt := "Enter the correct time shown on the pendulum clock:"
    Challenge.start_challenge(prompt, "Foyer", _validate_foyer)

func _validate_foyer(answer:String)->bool:
    return answer.to_lower() == Gamestate.clock_time.to_lower()


# ------------------ LOGIC ------------------
func _handle_foyer_action(action:String)->void:
    var room := "Foyer"

    match action:

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


        "F":
            var msg2 := "You see a large music note barely hanging on the wall. " \
            + "It is the note G, and it is the only one not covered in dust. " \
            + "On the back, an inscription reads: 'The key to the ballroom is in the music.'"

            Gamestate.modify_time(-5)
            Gamestate.mark_examined(room, "F")
            $Dialogue.show_text(msg2)


        "C":
            Gamestate.modify_time(-5)
            Gamestate.mark_examined(room, "C")
            $Dialogue.show_text("You examine the antique pendulum clock closely...")

        _:
            $Dialogue.show_text("Nothing happens.")


# ------------------ BUTTONS ------------------
func _on_brokenframe_pressed() -> void:
    _handle_foyer_action("F")
    RoomManager.check_room_completion()

func _on_large_chest_pressed() -> void:
    _handle_foyer_action("L")
    RoomManager.check_room_completion()

func _on_clock_pressed() -> void:
    if Gamestate.all_examined("Foyer", ["L","F","C"]):
        _start_foyer_challenge()
    else:
        $Dialogue.show_text("You feel like you haven't examined everything yet...")
    RoomManager.check_room_completion()

func _on_InventoryButton_pressed() -> void:
    $InventoryPanel.refresh_inventory()
    $InventoryPanel.visible = true


# ---------------------------------------------------------------
# HOVER ANIMATIONS
# ---------------------------------------------------------------
func _on_brokenframe_mouse_entered() -> void:
    $brokenframe/GlowAnimatorF.play("hover_on")

func _on_brokenframe_mouse_exited() -> void:
    $brokenframe/GlowAnimatorF.play("hover_off")

func _on_large_chest_mouse_entered() -> void:
    $"large chest"/GlowAnimatorL.play("hover_on")

func _on_large_chest_mouse_exited() -> void:
    $"large chest"/GlowAnimatorL.play("hover_off")

func _on_clock_mouse_entered() -> void:
    $clock/GlowAnimatorC.play("hover_on")

func _on_clock_mouse_exited() -> void:
    $clock/GlowAnimatorC.play("hover_off")
