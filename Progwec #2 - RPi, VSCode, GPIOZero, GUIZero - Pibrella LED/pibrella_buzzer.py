# Change History:
# 2020-03-10/ec:    Initial release.

from gpiozero import PWMOutputDevice
from guizero import App, PushButton
import time

def buzzer_on():
    buzzer.value = 0.5  # pwm duty cycle

def buzzer_off():
    buzzer.value = 0

buzzer = PWMOutputDevice(18, initial_value=0, frequency=440)

# === gui ===
app = App(title="Pibrella Buzzer")

button_on = PushButton(app, text="On", command=buzzer_on)
button_off = PushButton(app, text="Off", command=buzzer_off)
button_exit = PushButton(app, text="Exit", command=app.destroy)

app.display()
