extends CanvasLayer

@onready var timer = $Timer
@onready var bar = $ProgressBar  # change to $TextureProgressBar if needed

var target_value := 100.0

func _ready():
	bar.max_value = 100
	bar.value = 100

	# start timer if you want it automatic
	# timer.start()

func _process(delta):
	if timer.wait_time <= 0:
		return

	if timer.time_left > 0:
		# convert timer to percentage
		target_value = (timer.time_left / timer.wait_time) * 100.0
	else:
		target_value = 0

	# smooth movement (no jumping)
	bar.value = lerp(bar.value, target_value, 10.0 * delta)
