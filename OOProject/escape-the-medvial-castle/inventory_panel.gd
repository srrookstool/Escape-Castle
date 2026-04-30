extends Control

@onready var items_vbox = $ItemsVbox
@onready var notes_vbox = $NotesVbox
@onready var close_button = $close

func _ready():
	close_button.pressed.connect(_on_close_pressed)
	hide()

func _on_close_pressed():
	hide()

# ---------------------------------------------------------
# UNIVERSAL REFRESH — ITEMS + NOTES
# ---------------------------------------------------------
func refresh_inventory():
	_clear_vboxes()
	_display_items()
	_display_notes()


# ---------------------------------------------------------
# INTERNAL HELPERS
# ---------------------------------------------------------

func _clear_vboxes():
	for child in items_vbox.get_children():
		child.queue_free()
	for child in notes_vbox.get_children():
		child.queue_free()


func _display_items():
	if Gamestate.inventory.is_empty():
		var empty_label = Label.new()
		empty_label.text = "No items collected yet."
		items_vbox.add_child(empty_label)
		return

	for item in Gamestate.inventory:
		var label = Label.new()
		label.text = "• " + item
		items_vbox.add_child(label)


func _display_notes():
	if Gamestate.notes.is_empty():
		var empty_label = Label.new()
		empty_label.text = "No notes recorded yet."
		notes_vbox.add_child(empty_label)
		return

	var categories = Gamestate.notes.keys()
	categories.sort()   # ⭐ Godot 3.x sorting

	for category in categories:
		# Category header
		var cat_label = Label.new()
		cat_label.text = category + ":"
		cat_label.add_theme_color_override("font_color", Color(1, 0.85, 0.2))
		cat_label.add_theme_font_size_override("font_size", 18)
		notes_vbox.add_child(cat_label)

		# Entries under category
		for entry in Gamestate.notes[category]:
			var entry_label = Label.new()
			entry_label.text = "    - " + str(entry)
			notes_vbox.add_child(entry_label)
