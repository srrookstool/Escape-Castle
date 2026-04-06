extends Sprite2D


# Called when the node enters the scene tree for the first time.
func _ready():
	$glowL.modulate = Color(1, 1, 1, 0)
	$glowF.modulate = Color(1, 1, 1, 0)
	$glowC.modulate = Color(1, 1, 1, 0)
	
	$Dialogue.show_text("
Looking around... you find a way to access the castle, there is a huge staircase that branches off to the right and left. 
The door is huge and old, and when it opens, using a lot of force, it makes a creaking and frightening noise. 
Once inside, you admire a long red carpet, all worn and dirty, which reaches the foot of the stairs. 
						
To the left, next to the door, there is a coat rack, and to the right, there is a huge table with a chessboard on it. 
Behind the table, there is a fireplace that magically lights up once the door is opened. 
The room is dark, and the only source of light is the fireplace, which illuminates the entire room. 
						
In the left corner, you can admire a beautiful antique pendulum clock that reads the time of {clock_time}")



# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass


func _on_brokenframe_pressed() -> void:
	$Dialogue.show_text("You see a large music note barely hanging on the wall, it is the note G, and it is the only one that is not covered in dust. 
	You examine it, and you notice that there is a small inscription on the back of the note that says:
		 'The key to the ballroom is in the music...")


func _on_large_chest_pressed() -> void:
	$Dialogue.show_text("You see a large chest on the ground to your right 
	while brushing away spider webs you notice it looks old and worn,  
	but it might contain something useful-you open it...")


func _on_clock_pressed() -> void:
	$Dialogue.show_text("You walk up to the clock... it is frozen at midnight. 
	Something feels wrong.... 
	put the clock back at the correct time...")# Replace with function body.


func _on_brokenframe_mouse_entered() -> void:
	$brokenframe/GlowAnimatorF.play("hover_on")


func _on_brokenframe_mouse_exited() -> void:
	$brokenframe/GlowAnimatorF.play("hover_off")


func _on_large_chest_mouse_entered() -> void:
	$"large chest"/GlowAnimatorL.play("hover_onC")


func _on_large_chest_mouse_exited() -> void:
	$"large chest"/GlowAnimatorL.play("hover_offC")


func _on_clock_mouse_entered() -> void:
	$clock/GlowAnimatorC.play("hover_onL")


func _on_clock_mouse_exited() -> void:
	$clock/GlowAnimatorC.play("hover_offL")
