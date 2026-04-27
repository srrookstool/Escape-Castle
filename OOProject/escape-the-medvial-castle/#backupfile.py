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






#libray backup code
extends Sprite2D


# Called when the node enters the scene tree for the first time.
func _ready():
	$Dialogue.show_text("The large oak grandfather clock creaks as it opens... 
	you peak through, combing through spider webs to see walls lined with books,and another room with no way out.(insert door sliding old noise)
	
	
	You have now entered the library-
	it is covered in spider webs, and the only light is through the large window barley covered by fallen drapes. 
	
	The library is filled with old and worn books, some of them are so old that they are falling apart.
	There is a large wooden desk in the corner of the library, with a drawer that is slightly open with scattered papers and pens....")



# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass


func _on_romeoandjuliet_pressed() -> void:
	$Dialogue.show_text("You pull out a dusty copy of Romeo and Juliet, and as you open it, you see a piece of paper fall out-
	 it has an image of a rose on it, 
	and the words 'A rose by any other name would smell as sweet' written on it.")


func _on_sherlock_pressed() -> void:
	$Dialogue.show_text("You pull out a worn copy of The Great Gatsby, and as you open it, a piece of paper falls out- it has an image of a clock on it, and the words 'So we beat on, boats against the current, borne back ceaselessly into the past' written on it.")


func _on_gatsby_pressed() -> void:
	$Dialogue.show_text("You pull out a tattered copy of Sherlock Holmes, and as you open it, you see a piece of paper fall out- it has an image of a dagger on it, and the words 'When you have eliminated the impossible, whatever remains, however improbable, must be the truth' written on it.")


func _on_desk_pressed() -> void:
	$Dialogue.show_text("You study the framed picture on the desk... it must point to the correct book.")


func _on_frame_pressed() -> void:
	$Dialogue.show_text("You see a large music note barely hanging on the wall, you go closer to the, and it is covered in dust. You examine it, and you notice that there is a small inscription on the back of the note that says 'The key to the ballroom is in the music'.")
	
	
#glow animations

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



#backup ballroom gd
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




#backup final room
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
