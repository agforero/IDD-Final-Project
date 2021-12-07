#!/usr/bin/env python3

import busio
import board
import time
from adafruit_bus_device.i2c_device import I2CDevice
from struct import pack, unpack

# copper receiver library
import adafruit_mpr121

# set up button
DEVICE_ADDRESS = 0x6f  # device address of our button
STATUS = 0x03 # reguster for button status
AVAILIBLE = 0x1
BEEN_CLICKED = 0x2
IS_PRESSED = 0x4

i2c = busio.I2C(board.SCL, board.SDA)
device = I2CDevice(i2c, DEVICE_ADDRESS)

# button functions
def write_register(dev, register, value, n_bytes=1):
    # Write a wregister number and value
    buf = bytearray(1 + n_bytes)
    buf[0] = register
    buf[1:] = value.to_bytes(n_bytes, 'little')
    with dev:
        dev.write(buf)

def read_register(dev, register, n_bytes=1):
    # write a register number then read back the value
    reg = register.to_bytes(1, 'little')
    buf = bytearray(n_bytes)
    with dev:
        dev.write_then_readinto(reg, buf)
    return int.from_bytes(buf, 'little')

# clear out button LED lightning settings
write_register(device, 0x1A, 1)
write_register(device, 0x1B, 0, 2)
write_register(device, 0x19, 0)

# set up copper receiver
i2c2 = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c2)
gfl = [0 for _ in range(8)]

start_time = time.process_time()
gfl_times = [start_time for _ in range(8)]
cooldown = 0.05

global charKeys
with open("data/charDisplays.txt", 'r') as cf:
    raw = cf.read()
    charKeys = {}
    for line in raw.split("\n"):
        idx, val = tuple(line.split())
        charKeys[int(idx)] = val

# function for converting array to char
def arrToChar(arr):
    to_read = arr[::-1]
    ret = 0
    base = 1
    for i in range(8):
        ret += to_read[i] * base
        base *= 2

    return charKeys[ret]

# function for printing list as a single string
def arrToStr(arr):
    ret = ""
    for thing in arr:
        ret += str(thing)
    return ret

# reset data.txt
with open("data/data.txt", 'w') as r:
    r.write("00000000 null")

# main loop
while True:
    f = open("data/data.txt", 'a')
    # read in coppers
    for i in range(8):
        if (
            mpr121[i].value and
            ((time.process_time() - gfl_times[i]) > cooldown)
        ):
            gfl[i] = 0 if gfl[i] == 1 else 1
            gfl_times[i] = time.process_time()

    # get button input
    try:
        btn_status = read_register(device, STATUS)
        if (btn_status & IS_PRESSED) != 0:
            to_write = f"WRITING {arrToChar(gfl)}\n"
            f.write(to_write)
            #f.close()

            gfl = [0 for _ in range(8)]

    except KeyboardInterrupt:
        write_register(device, STATUS, 0)
        f.close()
        break

    time.sleep(0.05)
    #print(gfl)
    to_write = f"{arrToStr(gfl)} {arrToChar(gfl)}\n"
    f.write(to_write)
    f.close()
