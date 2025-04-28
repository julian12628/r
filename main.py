from microbit import *
import random

# Start positions
cue_x = 2
cue_y = 2
target_x = random.randint(0, 4)
target_y = random.randint(0, 4)

# Make sure target isn't on the cue ball
while target_x == cue_x and target_y == cue_y:
    target_x = random.randint(0, 4)
    target_y = random.randint(0, 4)

# Draw the balls
def draw():
    display.clear()
    display.set_pixel(cue_x, cue_y, 9)  # Cue ball (bright)
    display.set_pixel(target_x, target_y, 5)  # Target ball (dim)

draw()

while True:
    if button_a.is_pressed():
        cue_x = (cue_x - 1) % 5  # Move left
        draw()
        sleep(150)
    if button_b.is_pressed():
        cue_x = (cue_x + 1) % 5  # Move right
        draw()
        sleep(150)
    if accelerometer.was_gesture('up'):
        cue_y = (cue_y - 1) % 5  # Move up
        draw()
        sleep(150)
    if accelerometer.was_gesture('down'):
        cue_y = (cue_y + 1) % 5  # Move down
        draw()
        sleep(150)

    # Check if we "hit" the target ball
    if cue_x == target_x and cue_y == target_y:
        display.show(Image.HAPPY)
        sleep(2000)
        # Reset game
        cue_x = 2
        cue_y = 2
        target_x = random.randint(0, 4)
        target_y = random.randint(0, 4)
        while target_x == cue_x and target_y == cue_y:
            target_x = random.randint(0, 4)
            target_y = random.randint(0, 4)
        draw()
