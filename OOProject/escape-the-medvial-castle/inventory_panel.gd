extends Control

@onready var items_vbox = $ItemsVbox
@onready var notes_vbox = $NotesVbox
@onready var close_button = $close

func _ready():
	close_button.pressed.connect(_on_close_pressed)
	hide()

func _on_close_pressed():
	hide()

func refresh_inventory():
	# Clear old UI
	for child in items_vbox.get_children():
		child.queue_free()

	for child in notes_vbox.get_children():
		child.queue_free()

	# --- ITEMS ---
	for item in Gamestate.inventory:
		var label = Label.new()
		label.text = "- " + item
		items_vbox.add_child(label)

	# --- NOTES ---
	for category in Gamestate.notes.keys():
		var cat_label = Label.new()
		cat_label.text = category + ":"
		cat_label.add_theme_color_override("font_color", Color.YELLOW)
		notes_vbox.add_child(cat_label)

		for entry in Gamestate.notes[category]:
			var entry_label = Label.new()
			entry_label.text = "   • " + str(entry)
			notes_vbox.add_child(entry_label)
