from pymodbus.server.sync import StartSerialServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSparseDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer, ModbusBinaryFramer

import serial
import crc16
import time
import logging

FORMAT = ('%(asctime)-15s %(threadName)-15s'
          ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)


# print(crc16.crc16xmodem(b'123456789'))
# print(crc16.crc16xmodem(b"\x01\x06\x00\x01\x01\x00"))
# print(b"\x01\x06\x00\x01\x01\x00")


with serial.Serial(
    port='/dev/ttyUSB0', 
    baudrate=9600, 
    bytesize=serial.EIGHTBITS, 
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE
    ) as ser:
    ser.flush()

    
    print("Ligando")
    # Turn on - SLAVE 1
    # \xUnit_ID\0xFC\0xAdress\0xAdress\0xValue\0xValue\0xCRC16\0xCRC16
    # Adress, Value and CRC16 = 2 Bytes
    ser.write(b"\x01\x06\x00\x01\x01\x00\xD9\x9A")
    time.sleep(1)
    ser.write(b"\x01\x06\x00\x02\x01\x00\x29\x9A")
    time.sleep(1)
    ser.write(b"\x01\x06\x00\x03\x01\x00\x78\x5A")
    time.sleep(1)
    ser.write(b"\x01\x06\x00\x04\x01\x00\xC9\x9B")
    time.sleep(1)
    ser.write(b"\x01\x06\x00\x05\x01\x00\x98\x5B")
    time.sleep(1)
    ser.write(b"\x01\x06\x00\x06\x01\x00\x68\x5B")
    time.sleep(1)
    ser.write(b"\x01\x06\x00\x07\x01\x00\x39\x9B")
    time.sleep(1)
    ser.write(b"\x01\x06\x00\x08\x01\x00\x09\x98")
    time.sleep(1)
    

    # Turn on - SLAVE 2
    ser.write(b"\x02\x06\x00\x01\x01\x00\xD9\xA9")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x02\x01\x00\x29\xA9")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x03\x01\x00\x78\x69")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x04\x01\x00\xC9\xA8")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x05\x01\x00\x98\x68")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x06\x01\x00\x68\x68")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x07\x01\x00\x39\xA8")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x08\x01\x00\x09\xAB")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x09\x01\x00\x58\x6B")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x0A\x01\x00\xA8\x6B")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x0B\x01\x00\xF9\xAB")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x0C\x01\x00\x48\x6A")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x0D\x01\x00\x19\xAA")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x0E\x01\x00\xE9\xAA")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x0F\x01\x00\xB8\x6A")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x10\x01\x00\x89\xAC")
    time.sleep(5)


    # Turn on - SLAVE 5
    ser.write(b"\x05\x05\x00\x00\xFF\x00\xBE\x8D")
    time.sleep(1)
    ser.write(b"\x05\x05\x00\x01\xFF\x00\xDC\x7E")
    time.sleep(1)
    ser.write(b"\x05\x05\x00\x02\xFF\x00\x2C\x7E")
    time.sleep(1)
    ser.write(b"\x05\x05\x00\x03\xFF\x00\x7D\xBE")
    time.sleep(5)
 
   
    print("Desligando")
    # Turn off - SLAVE 1
    ser.write(b"\x01\x06\x00\x01\x02\x00\xD9\x6A")
    time.sleep(1)
    ser.write(b"\x01\x06\x00\x02\x02\x00\x29\x6A")
    time.sleep(1)
    ser.write(b"\x01\x06\x00\x03\x02\x00\x78\xAA")
    time.sleep(1)
    ser.write(b"\x01\x06\x00\x04\x02\x00\xC9\x6B")
    time.sleep(1)
    ser.write(b"\x01\x06\x00\x05\x02\x00\x98\xAB")
    time.sleep(1)
    ser.write(b"\x01\x06\x00\x06\x02\x00\x68\xAB")
    time.sleep(1)
    ser.write(b"\x01\x06\x00\x07\x02\x00\x39\x6B")
    time.sleep(1)
    ser.write(b"\x01\x06\x00\x08\x02\x00\x09\x68")
    time.sleep(1)

    

    # Turn off - SLAVE 2
    ser.write(b"\x02\x06\x00\x01\x02\x00\xD9\x59")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x02\x02\x00\x29\x59")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x03\x02\x00\x78\x99")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x04\x02\x00\xC9\x58")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x05\x02\x00\x98\x98")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x06\x02\x00\x68\x98")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x07\x02\x00\x39\x58")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x08\x02\x00\x09\x5B")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x09\x02\x00\x58\x9B")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x0A\x02\x00\xA8\x9B")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x0B\x02\x00\xF9\x5B")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x0C\x02\x00\x48\x9A")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x0D\x02\x00\x19\x5A")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x0E\x02\x00\xE9\x5A")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x0F\x02\x00\xB8\x9A")
    time.sleep(1)
    ser.write(b"\x02\x06\x00\x10\x02\x00\x89\x5C")
    time.sleep(5)


    # Turn off - SLAVE 5
    ser.write(b"\x05\x05\x00\x00\x00\x00\xCC\x4E")
    time.sleep(1)
    ser.write(b"\x05\x05\x00\x01\x00\x00\x9D\x8E")
    time.sleep(1)
    ser.write(b"\x05\x05\x00\x02\x00\x00\x6D\x8E")
    time.sleep(1)
    ser.write(b"\x05\x05\x00\x03\x00\x00\x3C\x4E")
    time.sleep(5)

 
    print("Analogico")
    # Read Proxsys Analog Input 1
    ser.write(b"\x05\x03\x00\x0E\x00\x01\x4D\xE4")
    # time.sleep(1)
    AnalogIn1 = ser.read(9)
    # AnalogIn1 = ser.read_until(expected=b'\n', size=None)
    # AnalogIn1 = ser.read_until(b'\n')
    print("EA 1 e 2")
    print(AnalogIn1)


    # Read Proxsys Analog Input 2
    ser.write(b"\x05\x03\x00\x0F\x00\x01\xB5\x8D")
    AnalogIn2 = ser.read(20)
    print(AnalogIn2)
