from djitellopy import tello

from time import sleep

me = tello.Tello()

me.connect()
print(me.get_battery())

me.takeoff()
me.send_rc_control(0, 29, 0, 0)

me.sleep(2)

me.send_rc_control(30, 0, 0, 0)

me.land()
