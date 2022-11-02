print("Hello, Pi Pico W!")
import ujson
import urequests
import network
import machine
import math
import dht
import time
import ubinascii
from smbus import SMBus

from BME280_pimironi import BME280
from LTR390 import LTR390
from OLED import OLED_2inch23

device_id = ubinascii.hexlify(machine.unique_id()).decode()
print(f"Device ID: {device_id}")

print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('', '')
while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.1)
print(" Connected!")

bus = SMBus(id=0, scl=machine.Pin(21), sda=machine.Pin(20), freq=100000)
env_sensor = BME280(i2c_dev=bus)
env_sensor.setup()
uv_sensor = LTR390()
OLED = OLED_2inch23()

try:
    while True:
        time.sleep(10)
        data = []
        env_sensor.calibration.set_temp_offset(-5.7)
        env_sensor.update_sensor()
        print("pressure : %7.2f hPa" % env_sensor.pressure)
        print("temp : %-6.2f ℃" % env_sensor.temperature)
        print("hum : %6.2f ％" % env_sensor.humidity)
        OLED.fill(0x0000) 
        OLED.text(f"Temp {env_sensor.temperature}",1,2,OLED.white)
        OLED.text(f"Humidity {env_sensor.humidity}",1,12,OLED.white)
        OLED.text(f"Pressure: {env_sensor.pressure}",1,22,OLED.white)  
        OLED.show()
        report_data = {
            "device_metadata": {
                "device_id": device_id,
                "name": "matt_d_pico_w_test",
            },
            "pressure": {
                "pressure": env_sensor.pressure,
                "unit": "hPa"
            },
            "temp": {
                "temp": env_sensor.temperature,
                "unit": "C"
            },
            "rh": {
                "rh": env_sensor.humidity,
            },
        }
        try:
            resp = urequests.post("https://opensensor.io/environment/",  headers = {'content-type': 'application/json'}, data=ujson.dumps(report_data))
            print(resp.text)
        except Exception as e:
            print(e)
        UVS = uv_sensor.UVS()
        print("UVS: %d" %UVS)
        
except KeyboardInterrupt:
    pass

