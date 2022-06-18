# Change History:
# 2020-03-22/ec:    Initial release.

from sense_hat import SenseHat
import sqlite3
import datetime
import time

sense = SenseHat()
sense.clear()

# === collect data ===

temp = sense.get_temperature()
hum = sense.get_humidity()
now = str(datetime.datetime.now())

# === insert to table ===

sql = ("insert into sensor_log ("
    + "    temperature,"
    + "    humidity,"
    + "    log_time"
    + ") values (?, ?, ?)")

conn = sqlite3.connect("/home/pi/sensehat/sensor.db")
conn.execute(sql, (temp, hum, now))
conn.commit()
conn.close()

print("{} {} {}".format(temp, hum, now))

for x in range(3):
    sense.clear(255, 165, 0)
    time.sleep(0.5)
    sense.clear()
    time.sleep(0.5)
