from listeners import led_listener, pump_listener
from sensor import Sensor
from firebase import add_listener
import path
from read_from_arduino import GasSensor

def main():
    add_listener(path.LED, led_listener)
    add_listener(path.PUMP, pump_listener)
    GasSensor.push_gas_to_firebase()

if __name__ == "__main__":
    try:
        main()
    except Exception:
        print('stopping programming')
        Sensor.clean_up()
        GasSensor.clean_up()
        print('programming stopped successfully')