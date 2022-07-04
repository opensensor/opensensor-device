# opensensor-device simulations
Working example wokwi simulation for prototyping the device software.

*Note:* The rapsberry pi nano w (with wi-fi) just came out and the v1 in wokwi simulation is lacking wifi support so we sub-out for the wokwi-esp32-devkit-v1 in this example.

The example does the following:
* Reads from a simulated wokwi-ntc-temperature-sensor the assigned attributes converted to an analog voltage.
* Connects to a wifi access point (simulated).
* Converts the voltage to a Celcius temperatue data.
* Uses micro requests to POST the data to a request bin (simulated server).
