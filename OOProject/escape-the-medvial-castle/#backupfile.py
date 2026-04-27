#backupfile

# BACKUP FOYER GD SCRIPT


extends Sprite2D

func _ready():
	$glowL.modulate = Color(1, 1, 1, 0)
	$glowF.modulate = Color(1, 1, 1, 0)
	$glowC.modulate = Color(1, 1, 1, 0)

	$Dialogue.show_text(
        "Looking around... you find a way to access the castle, 
        there is a huge staircase that branches off to the right and left, with a huge fountain in the center that emerges from the wall. 
        The door is huge and old, and when it opens, using a lot of force, it makes a creaking and frightening noise.
         Once inside, you admire a long red carpet, all worn and dirty, which reaches the foot of the stairs. 
         To the left, next to the door, there is a coat rack, and to the right, there is a huge table with a chessboard on it. 
         Behind the table, there is a fireplace that magically lights up once the door is opened. 
         The room is dark, and the only source of light is the fireplace, which illuminates the entire room. 
         In the left corner, you can admire a beautiful antique pendulum clock that reads the time of {clock_time}.\n\n"
	)


# ---------------------------------------------------------------
# API CALL FUNCTION
# ---------------------------------------------------------------
func send_action_to_api(letter: String, room_name: String):

	# ⭐ FIX: Cancel any stuck request so a new one can send
	if $HTTPRequest.get_http_client_status() != HTTPClient.STATUS_DISCONNECTED:
		$HTTPRequest.cancel_request()

	var body = {
		"room": room_name,
		"action": letter
	}

	$HTTPRequest.request(
		"http://127.0.0.1:8000/action",
		["Content-Type: application/json"],
		HTTPClient.METHOD_POST,
		JSON.stringify(body)
	)


# ---------------------------------------------------------------
# HANDLE API RESPONSE
# ---------------------------------------------------------------


func _on_http_request_request_completed(result: int, response_code: int, headers: PackedStringArray, body: PackedByteArray) -> void:
	print("FIRED")
	var text = body.get_string_from_utf8()
	var data = JSON.parse_string(text)
	print("DATA:", data)

	if typeof(data) == TYPE_DICTIONARY and data.has("message"):
		$Dialogue.show_text(data["message"])


# ---------------------------------------------------------------
# BUTTON INTERACTIONS
# ---------------------------------------------------------------
func _on_brokenframe_pressed() -> void:
	send_action_to_api("F", "Foyer")

func _on_large_chest_pressed() -> void:
	send_action_to_api("L", "Foyer")

func _on_clock_pressed() -> void:
	send_action_to_api("C", "Foyer")


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
