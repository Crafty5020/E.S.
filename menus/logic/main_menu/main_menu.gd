extends Node2D



func study_time_pressed():
	get_tree().change_scene_to_file("res://menus/study_time.tscn")

func exit_pressed():
	get_tree().quit(0)
