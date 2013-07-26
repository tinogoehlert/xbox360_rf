xbox360_rf
==========

Python Library for the Xbox 360 RF Module
------------------------------------------------------------

this Library allows you to control your Xbox 360 RF Module
with your RaspberryPi.  
It is written in Python and uses the [wiringPi2 Python library](https://github.com/Gadgetoid/WiringPi2-Python) .

Take a look at the example scrips or read the comments inside the library to get an idea how it works.

### RaspberryPi -> Xbox 360 RF Module wiring

GPIO 24 -> Data  (pin 6 on the module)  
GPIO 25 -> Clock (pin 7 on module)  
3V3:    -> VIN (USB)  
GND     -> GND  
