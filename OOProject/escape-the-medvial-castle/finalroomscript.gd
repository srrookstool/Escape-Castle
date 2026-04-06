extends Sprite2D


# Called when the node enters the scene tree for the first time.
func _ready():
	$Dialogue.show_text("… Once inside, visibility is very low, with light coming in through two windows with bars positioned very high up and out of reach. The dungeon is full of cobwebs and dust, and at the back, almost invisible, is a prison with pieces of rock forming a bench. The dungeon is full of covered and dusty objects. On the darkest side of the dungeon is an opening that allows only those who guess the code to find their way out...")



# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass


func _on_bench_pressed() -> void:
	$Dialogue.show_text("You see a bench made of rock in the corner of the dungeon, you walk over to examine it and you see a multiple carvings of combinations of the same four numbers from the notes all over the bench... what could this mean?")


func _on_table_pressed() -> void:
	$Dialogue.show_text("You see a covered table in the corner of the dungeon, you pull off the cover while coughing from the dust you drag the table tunder  the cellar doors hoping to reach the exit...")


func _on_cellar_pressed() -> void:
	$Dialogue.show_text("You uncover a set of cellar doors-hoping they head outside you think about what you have found so far- You try to piece together the clues and figure out the code to open the door. Enter your choices carefully as there may be a consequence... :")
