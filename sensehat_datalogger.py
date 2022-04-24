#!/usr =/bin/python
from sense_hat import SenseHat
import time
import datetime
import MySQLdb


db = MySQLdb.connect(host="localhost", user = "phpa", passwd = "*****", db = "SenseHat")
cur = db.cursor()
sense = SenseHat()


temperature = sense.get_temperature()
pressure = sense.get_pressure()
humidity = sense.get_humidity()

temp = round(0.0071*temperature*temperature+0.86*temperature-10.0,1)
humidity = round(humidity*(2.5-0.029*temperature),1)
pressure = round(pressure,1)
dt = (datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d"))
tm = (datetime.datetime.fromtimestamp(time.time()).strftime("%H:%M:%S"))
#sql = "insert into SenseHat Dt=%s, Tm=%s, Temperature=%s, Pressure=%s, Humidity=%s"
#cur.execute(sql, (time.strftime("%Y-%m-%d"), time.strftime("%H:%M:%s"), float(temperature), float(pressure), float(humidity)))
sql = "insert into SenseHatData (Dt, Tm, Temperature, Pressure, Humidity) values ('%s', '%s', '%f', '%f', '%f');" % (dt, tm, temp, pressure, humidity)



try:
    cur.execute(sql)
    db.commit()
    #db.close()
except:
    db.rollback()

