extends Sprite2D

@onready var Challenge = get_node("Challenge")

func _ready():
    Gamestate.current_room_index = 3

    var desc := "Once inside, visibility is very low. Light slips in through two barred windows..." \
    + "\n\nOn the darkest side of the dungeon is an opening — only those who guess the code may escape."

    $Dialogue.show_text(desc)


# ---------------------------------------------------------
# CHALLENGE
# ---------------------------------------------------------
func _start_dungeon_challenge():
    var prompt := "Enter the final 4‑digit escape code:"

    var validator := func(answer:String) -> bool:
        return answer.strip_edges() == Gamestate.door_code

    Challenge.start_challenge(prompt, "Dungeon", validator)


# ---------------------------------------------------------
# LOGIC
# ---------------------------------------------------------
func _handle_dungeon_action(letter:String)->void:
    var room := "Dungeon"
    var required := ["B","T"]

    match letter:

        "B":
            var msg := "You examine the stone bench. Carvings of familiar numbers cover its surface."
            Gamestate.modify_time(-5)
            Gamestate.mark_examined(room, "B")
            Gamestate.mark_clue_inspected(room, "B")
            $Dialogue.show_text(msg)

        "T":
            var msg2 := "You uncover a dusty table and drag it under the cellar doors."
            Gamestate.modify_time(-5)
            Gamestate.mark_examined(room, "T")
            Gamestate.mark_clue_inspected(room, "T")
            $Dialogue.show_text(msg2)

        "D":
            # Already solved?
            if Gamestate.is_puzzle_solved(room):
                $Dialogue.show_text("The cellar doors are already unlocked — you've solved this puzzle.")
                return

            # Not all examined yet
            if not Gamestate.all_examined(room, required):
                $Dialogue.show_text("You feel like you haven't examined everything yet...")
                return

            # All examined → start challenge
            if not Challenge.visible:
                _start_dungeon_challenge()

        _:
            $Dialogue.show_text("Nothing happens.")


# ---------------------------------------------------------
# BUTTONS
# ---------------------------------------------------------
func _on_bench_pressed():
    _handle_dungeon_action("B")

func _on_table_pressed():
    _handle_dungeon_action("T")

func _on_cellar_pressed():
    _handle_dungeon_action("D")

func _on_inventory_pressed():
    $InventoryPanel.refresh_inventory()
    $InventoryPanel.visible = true


# ---------------------------------------------------------
# HOVER ANIMATIONS
# ---------------------------------------------------------
func _on_cellar_mouse_entered() -> void:
    $cellar/AnimationPlayerC.play("hover_onC")

func _on_cellar_mouse_exited() -> void:
    $cellar/AnimationPlayerC.play("hover_offC")

func _on_table_mouse_entered() -> void:
    $table/AnimationPlayerT.play("hover_onT")

func _on_table_mouse_exited() -> void:
    $table/AnimationPlayerT.play("hover_offT")

func _on_bench_mouse_entered() -> void:
    $bench/AnimationPlayerB.play("hover_onB")

func _on_bench_mouse_exited() -> void:
    $bench/AnimationPlayerB.play("hover_offB")

func _on_inventory_mouse_entered() -> void:
    $Inventory/GlowInv.play("hover_onI")

func _on_inventory_mouse_exited() -> void:
    $Inventory/GlowInv.play("hover_offI")
