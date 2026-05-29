extends Area2D

func _on_input_event(viewport, event, shape_idx):
	if event is InputEventMouseButton and event.pressed:
		modulate = Color(0, 0, 1)  
