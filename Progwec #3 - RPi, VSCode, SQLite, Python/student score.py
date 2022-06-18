# Change History:
# 2020-03-17/ec:    Initial release.

import sqlite3
from guizero import App, Text, PushButton, Box, TextBox

def show_score():
    global box_score
    box_score.destroy()
    box_score = Box(app, grid=[0, 2, 2, 1], layout="grid")

    text_status.value = ""

    if (text_student.value.isnumeric()):
        student_number = int(text_student.value)
    else:
        text_status.value = ("Invalid student number: " 
            + text_student.value)
        return

    conn = sqlite3.connect("student_score.db")
    cur = conn.cursor()
    cur.execute(sql, (student_number, ))
    rows = cur.fetchall()   # only when result set is small
    conn.close()

    if len(rows) == 0:
        text_status.value = ("Student number not found: " 
            + text_student.value)
    else:
        Text(box_score, "Student Number", grid=[0, 0], width=15)
        Text(box_score, "Class Number", grid=[1, 0], width=12)
        Text(box_score, "Score", grid=[2, 0], width=8, align="right")

        y = 0

        for row in rows:
            y += 1
            Text(box_score, text=row[0], grid=[0, y])
            Text(box_score, text=row[1], grid=[1, y])
            Text(box_score, text=row[2], grid=[2, y], align="right")

sql = (" select "
    + "     student_number,"
    + "     class_number,"
    + "     test_score"
    + " from score"
    + " where student_number = ?"
    + " order by class_number")

# === gui ===
app = App("Grid Demo", layout="grid")

Text(app, text="Enter Student Number:", grid=[0, 0])
text_student = TextBox(app, grid=[1, 0])
button_show = PushButton(app, text="Show Score",
    grid=[0, 1, 2, 1], command=show_score)
box_score = Box(app, layout="grid", grid=[0, 2, 2, 1])
PushButton(app, text="Exit", grid=[0, 3, 2, 1], command=app.destroy)
text_status = Text(app, text="Ready", align="left", grid=[0, 4, 2, 1])

app.display()
