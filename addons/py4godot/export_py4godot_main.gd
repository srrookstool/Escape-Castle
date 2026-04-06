@tool
extends EditorPlugin

var export_plugin

func _enter_tree():
    # Carica la logica di export originale
    export_plugin = preload("res://addons/py4godot/export_py4godot.gd").new()
    add_export_plugin(export_plugin)
    
    # Sintassi corretta per Godot 4: 
    # Il secondo argomento deve essere un Callable diretto
    add_tool_menu_item("Export Py4Godot Project", _on_export_menu_pressed)

func _exit_tree():
    if export_plugin:
        remove_export_plugin(export_plugin)
        export_plugin = null
    
    # Rimuove la voce dal menu
    remove_tool_menu_item("Export Py4Godot Project")

# Questa funzione viene chiamata quando clicchi sul menu
func _on_export_menu_pressed():
    print("Avvio esportazione Py4Godot...")
    # Se vuoi far apparire un messaggio a schermo:
    OS.alert("Funzione di Export attivata!", "Py4Godot")