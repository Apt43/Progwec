# Change History:
# 2020-02-19/ec:    Initial release.

from gpiozero import LED
from guizero import App, Text, PushButton

led = LED(gpio)

def turn_on():
    led.blink()

def turn_off():
    led.off()

# === gui ===
app = App(title="Hello GPIO!")

text = Text(app, text="Hello GPIO!")
button_on = PushButton(app, text="On", command=turn_on)
button_off = PushButton(app, text="Off", command=turn_off)
button_exit = PushButton(app, text="Exit", command=app.destroy)

app.display()
