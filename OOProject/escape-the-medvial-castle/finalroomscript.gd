extends Sprite2D

func _ready():
    $Dialogue.show_text(
        "Once inside, visibility is very low. Light slips in through two barred windows "
        "positioned high above your reach. The dungeon is thick with cobwebs and dust.\n\n"
        "At the back, almost invisible, is a small prison cell with pieces of rock forming a bench. "
        "Covered and forgotten objects fill the room.\n\n"
        "On the darkest side of the dungeon is an opening — only those who guess the code "
        "may find their way out..."
    )


# ---------------------------------------------------------
# API CALL FUNCTION
# ---------------------------------------------------------
func send_action_to_api(letter: String, room_name: String):
    var body = {
        "room": room_name,
        "action": letter
    }

    $HTTPRequest.request(
        "http://127.0.0.1:8000/action",
        [],
        true,
        HTTPClient.METHOD_POST,
        JSON.stringify(body)
    )


# ---------------------------------------------------------
# HANDLE API RESPONSE
# ---------------------------------------------------------
func _on_HTTPRequest_request_completed(result, code, headers, body):
    var data = JSON.parse_string(body)
    if typeof(data) == TYPE_DICTIONARY:
        $Dialogue.show_text(data.message)


# ---------------------------------------------------------
# BUTTON INTERACTIONS (API CALLS)
# ---------------------------------------------------------

func _on_bench_pressed() -> void:
    send_action_to_api("B", "Dungeon")

func _on_table_pressed() -> void:
    send_action_to_api("T", "Dungeon")

func _on_cellar_pressed() -> void:
    send_action_to_api("D", "Dungeon")


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
