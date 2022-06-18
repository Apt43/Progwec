# Change History:
# 2020-02-15/ec:    Initial release.

from gpiozero import PWMLED
from guizero import App, PushButton, Text, Slider

def slider_green_changed():
    led_green.value = slider_green.value / 100

def slider_amber_changed():
    led_amber.value = slider_amber.value / 100

def slider_red_changed():
    led_red.value = slider_red.value / 100

led_green = PWMLED(4)
led_amber = PWMLED(17)
led_red = PWMLED(27)

# === gui ===

app = App(title="Pibrella LED Dim", layout="grid")
text_title = Text(app, 
    text="Use slider to change brightness % of LED:", 
    grid=[0, 0, 2, 1])

text_green = Text(app, text="Green", grid=[0, 1])
slider_green = Slider(app, start=0, end=100,
    command=slider_green_changed, grid=[1, 1])
text_amber = Text(app, text="Amber", grid=[0, 2])
slider_amber = Slider(app, start=0, end=100,
    command=slider_amber_changed, grid=[1, 2])
text_red = Text(app, text="Red", grid=[0, 3])
slider_red = Slider(app, start=0, end=100,
    command=slider_red_changed, grid=[1, 3])

button_exit = PushButton(app, text="Exit",
    command=app.destroy, grid=[0, 4, 2, 1])

app.display()
