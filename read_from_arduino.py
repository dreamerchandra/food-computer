import serial
from separate_thread import seprate_thread
import json
from firebase import push_val
import path


class GasSensor:
    GasSensor._ser = serial.Serial('/dev/ttyACM0')
    GasSensor._ser.flushInput()
    GasSensor.cvt_raw_to_int = lambda raw_dict: [int(val) for val in json.loads(raw_dict).values()]
    
    @staticmethod
    def clean_up():
        print("closing connection with arduino")
        GasSensor._ser.close()

    @staticmethod
    @seprate_thread()
    def push_gas_to_firebase():
        while True:
          try:
            raw_data = GasSensor._ser.readline()
            humidity, temperature = GasSensor.cvt_raw_to_int(raw_data)
            print('values from arduino>>> \n raw_data: {}\n humidity {}, temp'.format(raw_data, humidity, temperature))
            push_val(path.GAS, json.loads(raw_data))
        except:
            GasSensor.clean_up()