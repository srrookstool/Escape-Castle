extends Sprite2D


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	$glow.modulate = Color(1, 1, 1, 0)




func _on_startbutton_pressed() -> void:
	get_tree().change_scene_to_file("res://escapecastleMain.tscn")


func _on_startbutton_mouse_entered() -> void:
	$startbutton/GlowAnimator.play("hover_on")



func _on_startbutton_mouse_exited() -> void:
	$startbutton/GlowAnimator.play("hover_off")
