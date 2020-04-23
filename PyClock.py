import eel
import datetime
import time

eel.init('web') #directory

@eel.expose
def ang(unit):  #angle secod
    time.sleep(0.007)
    now = datetime.datetime.now()

    if unit == "now.hour":
        return 360/12 * eval(unit) - 90

    elif unit== "now.microsecond":
        return  (360/60 * (now.second + now.microsecond/1000000)) - 90

    else:
        return 360/60 * eval(unit) - 90


eel.start('main.html', block=False, size=(500, 500))

while True:
    eel.sleep(1.0)