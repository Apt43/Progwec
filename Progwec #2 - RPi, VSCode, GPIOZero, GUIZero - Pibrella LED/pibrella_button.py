# Change History:
# 2020-03-10/ec:    Initial release

from gpiozero import LED, Button

def button_on():
    led_green.on()

def button_off():
    led_green.off()

button = Button(11, pull_up=False)  # *** pull_up must be False ***
button.when_pressed = button_on
button.when_released = button_off

led_green = LED(4)

print("Press and hold the Button on Pibrella to turn on LED.")
input("Press Enter to Exit.")
print("Bye!")
