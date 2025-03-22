extends Node2D

var classes
var time

func classes_changed(new_text):
	new_text = float(new_text)
	if new_text != null and typeof(new_text) == TYPE_FLOAT:
		classes =  new_text
		calculate_time()
	else:
		$error.text = "ERROR: input from 'how many classes' must be a number"
		$show_error_time.start()
		await $show_error_time.timeout
		$error.text = ""


func time_changed(new_text):
	new_text = float(new_text)
	if new_text != null and typeof(new_text) == TYPE_FLOAT:
		time = new_text
		calculate_time()
	else:
		$error.text = "ERROR: input from 'how much time' must be a number"
		$show_error_time.start()
		await $show_error_time.timeout
		$error.text = ""

func calculate_time():
	if classes != null and time != null and typeof(classes) == TYPE_FLOAT and typeof(time) == TYPE_FLOAT and classes != 0 and time != 0:
		var result = time/classes
		# Convert result to hours, minutes, and seconds
		var hours = int(result)
		var minutes = int((result - hours) * 60)
		var seconds = int((((result - hours) * 60) - minutes) * 60)

		# Format the time properly
		$result.text = "%02d:%02d:%02d" % [hours, minutes, seconds]
	else:
		$result.text = "00:00:00"


func x_pressed():
	get_tree().change_scene_to_file("res://menus/main_menu.tscn")
