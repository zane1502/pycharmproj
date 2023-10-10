from djitellopy import tello
import keypressmodules as kp
import time
import cv2

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
global img
me.streamon()

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): ud = -speed
    elif kp.getKey("DOWN"): ud = speed

    if kp.getKey("w"): fb = speed
    elif kp.getKey("s"): fb = -speed

    if kp.getKey("q"): me.land();
    time.sleep(3)
    if kp.getKey("t"): me.takeoff()

    if kp.getKey('z'):
        cv2.imwrite(f'Resources/Images/{time.time()}')
        time.sleep(0.5)
 
    return [lr, fb, ud, yv]

while True:

    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = me.get_frame_read().frame
    cv2.resize(img, (360, 240))
    cv2.imshow('Display', img)
    cv2.waitKey(1)
