import djitellopy as tello
import cv2
import keypressmodules as kp
from time import sleep
import numpy as np
import math

### parameters ####

fSpeed = 30 # forward speed in cm/s
aSpeed = 36 # angular speed in deg/s
interval = 0.25

dInterval = fSpeed * interval
aInterval = aSpeed * interval

#####################

x, y = 500, 500
a = 0
yaw = 0

kp.init()

drone = tello.Tello()
drone.connect()
battery = drone.get_battery()

print(drone.get_battery())
points = []

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0

    speed = 15
    speed
    global x, y, yaw, a
    d = 0


    if kp.getKey('LEFT'):
        lr = -speed
        d = dInterval
        a = -180

    elif kp.getKey('RIGHT'):
        lr = speed
        d = dInterval
        a = 180

    if kp.getKey('UP'):
        fb = speed
        d = dInterval
        a = 270

    elif kp.getKey('DOWN'):
        fb = -speed
        d = dInterval
        a = -90

    if kp.getKey('u'):
        ud = speed
    elif kp.getKey('d'):
        ud = -speed


    if kp.getKey('y'):
        yv = speed
        yaw -= aInterval

    elif kp.getKey('z'):
        yv = -speed
        yaw += -aInterval
    if kp.getKey('t'):
        drone.takeoff()
    if kp.getKey('l'):
        drone.land()

    sleep(interval)

    a += yaw
    x += int(d*math.cos(math.radians(a)))
    y += int(d*math.sin(math.radians(a)))


    return [lr, fb, ud, yv, x, y]

def drawPoints():

    for point in points:
        cv2.circle(img, points, 7, (0, 0, 255), cv2.FILLED)
    cv2.putText(img, f'({points[-1][0]-500/100})m',
                (points[-1][0]+ 10, points[-1][1] + 30))


while True:
    vals = getKeyboardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = np.zeros((1000, 1000, 3), np.uint8)
    points.append((vals[4], vals[5]))
    drawPoints(img, points)
    cv2.imshow("Output", img)
    cv2.waitKey(1)
