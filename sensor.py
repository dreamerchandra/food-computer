import RPi.GPIO as GPIO
import pin as PIN
import serial

ser = serial.Serial('/dev/ttyACM0')
ser_bytes = ser.readline()

GPIO.setmode(GPIO.BCM)

class PinStatus:
    def __init__(self, pin, is_high):
        self.pin = pin
        self.status = is_high

class Sensor:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    led = PinStatus(PIN.LED, False)
    GPIO.setup(led.pin, GPIO.OUT)
    pump = PinStatus(PIN.PUMP, False)
    GPIO.setup(pump.pin, GPIO.OUT)
    print ('GPIO initialized');
    
    @staticmethod
    def toggle_led():
        GPIO.output(Sensor.led.pin, GPIO.LOW if Sensor.led.status else GPIO.HIGH)
        Sensor.led.status = not Sensor.led.status
        print ('led current status', Sensor.led.status)
    
    @staticmethod
    def toggle_pump():
        GPIO.output(Sensor.pump.pin, GPIO.LOW if Sensor.pump.status else GPIO.HIGH)
        Sensor.pump.status = not Sensor.pump.status
        print ('pump current status', Sensor.pump.status)

    @staticmethod
    def clean_up():
        GPIO.cleanup()
        print ('cleaned up gpio')
