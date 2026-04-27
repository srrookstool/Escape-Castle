extends Sprite2D

func _ready():
    $Dialogue.show_text(
        "As you walk down the spiraling stairs, a golden light begins to appear. "
        "You hear the faint sound of classical music echoing through the stone walls.\n\n"
        "The stairs lead you to a small wooden door with a tiny window. "
        "You push it open and step into the ballroom..."
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

func _on_piano_pressed() -> void:
    send_action_to_api("P", "Ballroom")

func _on_frames_pressed() -> void:
    send_action_to_api("F", "Ballroom")

func _on_note_pressed() -> void:
    send_action_to_api("N", "Ballroom")


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
