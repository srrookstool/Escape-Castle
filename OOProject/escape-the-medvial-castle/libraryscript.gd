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
