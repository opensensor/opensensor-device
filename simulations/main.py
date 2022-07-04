print("Hello, Pi Pico W!")
import ujson
import urequests
import network
import machine
import math
import dht
import time

adc = machine.ADC(machine.Pin(4))
analog_value = adc.read_u16()
print(analog_value)
BETA = 3950 # should match the Beta Coefficient of the thermistor
celsius = 1 / (math.log(1 / (65535 / analog_value - 1)) / BETA + 1.0 / 298.15) - 273.15
print(f"The temperature is: {celsius}")

print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.1)
print(" Connected!")

data = {"temp": celsius, "unit": "C"}
resp = urequests.post("https://requestbin.io/v1nc48v1",  headers = {'content-type': 'application/json'}, data=ujson.dumps(data))
print(resp.text)