# Change History:
# 2020-02-19/ec:    Initial release.

from guizero import App, Text, PushButton

# === gui ===
app = App(title="Hello GUI!")

text = Text(app, text="Hello GUI!")
button_exit = PushButton(app, text="Bye!", command=app.destroy)

app.display()
