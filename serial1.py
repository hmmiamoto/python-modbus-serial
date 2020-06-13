import serial

with serial.Serial(port='/dev/ttyUSB0', 
    baudrate=9600, 
    bytesize=serial.EIGHTBITS, 
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE
    ) as ser:
    ser.flush()
    # Turn off
    ser.write(b"\x01\x06\x00\x02\x02\x00\x29\x6A")
    input()
    # Turn on
    ser.write(b"\x01\x06\x00\x02\x01\x00\x29\x9A")