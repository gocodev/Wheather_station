# Complete project details at https://RandomNerdTutorials.com
import wifimgr

try:
  import usocket as socket
except:
  import socket

from time import sleep

from machine import Pin, I2C
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

import BME280

# ESP8266 - Pin assignment
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)

wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D


# Main Code goes here, wlan is a working network.WLAN(STA_IF) instance.
print("ESP OK")

"""
ssid = 'NETIASPOT-2.4GHz-9MAN'
password = 'PbkT3e8d'

#ssid = 'Dom'
#password = '663747858'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)


while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
"""
