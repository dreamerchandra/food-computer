from sensor import Sensor

def led_listener(event):
    if event.data is 1 or event.data is 0:
        print ('led gng to turn on')
        Sensor.toggle_led()

def pump_listener(event):
    if event.data is 1 or event.data is 0:
        print ('pump gng to turn on')
        Sensor.toggle_pump()