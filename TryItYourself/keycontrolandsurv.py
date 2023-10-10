from djitellopy import tello
import keypressmodules as kp
import cv2
import time

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())


me.streamon()
global img

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50


    if kp.getKey('LEFT'):
        lr = -speed
    elif kp.getKey('RIGHT'):
        lr = speed
    if kp.getKey('UP'):
        ud = speed
    elif kp.getKey('DOWN'):
        ud = -speed
    if kp.getKey('a'):
        yv = -speed
    elif kp.getKey('d'):
        yv = speed
    if kp.getKey('t'):
        me.takeoff()
    if kp.getKey('l'):
        me.land()

    if kp.getKey('p'):
        cv2.imwrite(f'File/Images/{time.time()}.jpg', img)

    return [lr, fb, ud, yv]

while True:

    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow('Drone Feed', img)
    cv2.waitKey(1)

