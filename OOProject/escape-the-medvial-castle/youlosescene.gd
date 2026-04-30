extends Node2D


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass


func _on_restartbutton_mouse_entered() -> void:
	$restartbutton/GlowAnimator.play("hover_on")



func _on_restartbutton_mouse_exited() -> void:
	$restartbutton/GlowAnimator.play("hover_off")

func _on_restartbutton_pressed() -> void:
	get_tree().change_scene_to_file("res://escapecastleMain.tscn")
