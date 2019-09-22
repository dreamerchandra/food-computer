import serial
from separate_thread import seprate_thread
import json
from firebase import push_val
import path


class GasSensor:
    _ser = serial.Serial('/dev/ttyACM0')
    _ser.flushInput()
    cvt_raw_to_float = lambda raw_dict: [float(val) for val in eval(raw_dict).values()]
    
    @staticmethod
    def clean_up():
        print("closing connection with arduino")
        GasSensor._ser.close()

    @staticmethod
    @seprate_thread()
    def push_gas_to_firebase():
        while True:
          try:
            raw_data = str(GasSensor._ser.readline().decode("utf-8").strip('\n').strip('\r'))
            print (raw_data)
            co2, humidity = GasSensor.cvt_raw_to_float(raw_data)
            print('values from arduino>>> \n raw_data: {}\n humidity {}, co2: {}'.format(raw_data, humidity, co2))
            push_val(path.GAS, eval(raw_data))
          except:
            GasSensor.clean_up()
            break
            return