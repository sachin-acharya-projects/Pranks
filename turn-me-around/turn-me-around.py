import rotatescreen
import time

screen = rotatescreen.get_primary_display()
start = screen.current_orientation

print(start)
if not start == 0:
    screen.rotate_to(0)
else:
    for i in range(1, 10):
        a = abs((start - i * 90) % 360)
        screen.rotate_to(a)
        time.sleep(1)
