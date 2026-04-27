extends Control

func _ready():
    refresh_inventory()

func refresh_inventory():
    # Clear old entries
    for child in $ItemsVBox.get_children():
        child.queue_free()

    for child in $NotesVBox.get_children():
        child.queue_free()

    # Add items
    for item in Gamestate.inventory:
        var label := Label.new()
        label.text = "• " + item
        $ItemsVBox.add_child(label)

    # Add notes
    for category in Gamestate.notes.keys():
        var entries = Gamestate.notes[category]
        var label := Label.new()
        label.text = "%s: %s" % [category, ", ".join(entries)]
        $NotesVBox.add_child(label)

func _on_CloseButton_pressed():
    visible = false
