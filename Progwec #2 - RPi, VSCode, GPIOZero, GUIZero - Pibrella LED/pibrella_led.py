# Change History:
# 2020-02-15/ec:    Initial release.

from gpiozero import LED
from guizero import App, CheckBox, PushButton, Text

def led_on_off(check_box, led):
    if check_box.value == 1:
        led.blink()    # change on to blink, to make led blink
    else:
        led.off()

def check_green_clicked():
    led_on_off(check_green, led_green)

def check_amber_clicked():
    led_on_off(check_amber, led_amber)

def check_red_clicked():
    led_on_off(check_red, led_red)

led_green = LED(4)
led_amber = LED(17)
led_red = LED(27)

# === gui ===

app = App(title="Pibrella LED On/Off")

text_message = Text(app, text="Click check box to turn on/off LED:")

check_green = CheckBox(app, text="Green", command=check_green_clicked)
check_amber = CheckBox(app, text="Amber", command=check_amber_clicked)
check_red = CheckBox(app, text="Red", command=check_red_clicked)

button_exit = PushButton(app, text="Exit", command=app.destroy)

app.display()
