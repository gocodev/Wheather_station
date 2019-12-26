
# Complete project details at https://RandomNerdTutorials.com

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

def web_page():
  bme = BME280.BME280(i2c=i2c)
  
  html = """<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"><style>body { text-align: center; font-family: "Trebuchet MS", Arial;}
  table { border-collapse: collapse; width:35%; margin-left:auto; margin-right:auto; }
  th { padding: 12px; background-color: #0043af; color: white; }
  tr { border: 1px solid #ddd; padding: 12px; }
  tr:hover { background-color: #bcbcbc; }
  td { border: none; padding: 12px; }
  .sensor { color:white; font-weight: bold; background-color: #bcbcbc; padding: 1px;
  </style></head><body><h1>Bezprzewodowa stacja pogodowa</h1>
  <table><tr><th>Pomiar</th><th>Wartość</th></tr>
  <tr><td>Temp. &#176C</td><td><span class="sensor">""" + str(bme.temperature) + """</span></td></tr>
  <tr><td>Temp. &#176F</td><td><span class="sensor">""" + str(round((bme.read_temperature()/100.0) * (9/5) + 32, 2))  + """F</span></td></tr>
  <tr><td>Ciśnienie</td><td><span class="sensor">""" + str(bme.pressure) + """</span></td></tr>
  <tr><td>Wilgotność</td><td><span class="sensor">""" + str(bme.humidity) + """</span></td></tr></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  try:
    if gc.mem_free() < 102000:
      gc.collect()
    conn, addr = s.accept()
    conn.settimeout(3.0)
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    conn.settimeout(None)
    request = str(request)
    print('Content = %s' % request)
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
  except OSError as e:
    conn.close()
    print('Connection closed')

