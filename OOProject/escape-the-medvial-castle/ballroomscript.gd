extends Sprite2D


# Called when the node enters the scene tree for the first time.
func _ready():
	$Dialogue.show_text("... As you are walking down the spiraling stairs, 
	you start to see a golden light appear and the faint sound of.... Classical music? 
	- the stairs led you to a small door with a small looking window, you entered to find the ballroom.")



# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass


func _on_piano_pressed() -> void:
	$Dialogue.show_text("You see a grand piano in the corner of the ballroom, it is covered in dust, but it looks like it is still functional. 
	You sit down and start to play the notes you found in the foyer and library, and as you play, 
	you notice that the music starts to change...")

func _on_frames_pressed() -> void:
	$Dialogue.show_text("You see a large shattered frames barely hanging on the wall, 
	the are images of music notes, they contain the notes C and E, and it is the only one that is not covered in dust.
	 You examine it, and you notice that there is a small inscription on the back of the note that says 'The key to the ballroom is in the music'.")


func _on_note_pressed() -> void:
	$Dialogue.show_text("You see a small ripped note on the ground, badly worn, 
	you pick it up and read the numbers on it- it contains two digits - 
	piece of paper for the final code: {door_code[:2]}.")
