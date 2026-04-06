extends Control


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass

@onready var label = $RichTextLabel

func show_text(text):
	label.visible_characters = 10000
	label.text = text
	visible = true
	$AnimationPlayer.play("typewriter")
