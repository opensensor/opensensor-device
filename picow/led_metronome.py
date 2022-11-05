import machine
import utime
import time

led_external = machine.Pin(15, machine.Pin.OUT)
switch = machine.Pin(14, machine.Pin.IN)
duration = 2.0
start_time = None
def callback(p):
    global start_time
    global duration
    print('pin change', p)
    if start_time is None:
        start_time = time.ticks_ms()
    else:
        duration = (time.ticks_ms() - start_time)/1000
        start_time = None

switch.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=callback)
    
#print(switch.value())
#while switch.value():
#    pass
#start_time = utime.time()
#while not switch.value():
#    pass
#end_time = utime.time()
#duration = end_time - start_time


while True:
    led_external.toggle()
    print(duration)
    time.sleep(duration)

