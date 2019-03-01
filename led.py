from gpiozero import LED, Button
from signal import pause

led = LED(25)
button = Button(3)

button.when_pressed = led.on
button.when_released = led.off

pause()
