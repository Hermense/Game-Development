extends Node2D

func _process(delta):
	for child in get_children():
		if child is Area2D:
			child.rotation += 1.5 * delta

func _input(event):
	if event.is_action_pressed("color_1"):
		$Area2D1.modulate = Color(1, 0, 0) 
	elif event.is_action_pressed("color_2"):
		$Area2D2.modulate = Color(0, 1, 0)  
	elif event.is_action_pressed("color_3"):
		$Area2D3.modulate = Color(0, 0, 1)  
