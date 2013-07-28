# xbox_rf.py
# 
# A Python library to control Xbox 360 RF Units 
# with an Raspberry Pi.
#
# Created by Tino Goehlert
# 
# www.astrorats.org | @_tin0_

import wiringpi2

data_pin  = 5 # data line (pin 6 on the module)
clock_pin = 6 # clock line (pin 7 on module)


cmdlist = {} # Simple lookup Table with presotred Commands 

#Activates/initialises the LEDs, leaving the center LED lit.
cmdlist["led_cmd"]   = "0010000100"
#Makes the startup animation on the ring of light.
cmdlist["anim_cmd"]  = "0010000101"

#Green LED control - ordered clockwise
cmdlist["green_ul"]  = "0010100001"
cmdlist["green_ur"]  = "0010100010"
cmdlist["green_dr"]  = "0010101000"
cmdlist["green_dl"]  = "0010100100"

#Red LED control - ordered clockwise
cmdlist["red_ul"]    = "0010110001"
cmdlist["red_ur"]    = "0010110010"
cmdlist["red_dr"]    = "0010111000"
cmdlist["red_dl"]    = "0010110100"

#Initiates the sync process.
cmdlist["ctl_sync"]  = "0000000100"
#Shutdown controllers remotely.
cmdlist["ctl_shutdown"]  = "0000001001"

# Reverse cmdlist. Needed by Bruteforce to resolv 
# binary commands to their names.
cmdlist_reversed = dict([(v,k) for k,v in cmdlist.items()])


# SendData
#   Sends a Command to the Module
def SendData(command, delay = 0):
  wiringpi2.pinMode(data_pin,1)
  wiringpi2.digitalWrite(data_pin,0)

  prev = 1
  for i in range(len(command)):

    while prev == wiringpi2.digitalRead(clock_pin):
        pass

    prev = wiringpi2.digitalRead(clock_pin)
    wiringpi2.digitalWrite(data_pin, int(command[i]))

    while prev == wiringpi2.digitalRead(clock_pin):
        pass

    prev = wiringpi2.digitalRead(clock_pin)

  wiringpi2.digitalWrite(data_pin, 1)
  wiringpi2.pinMode(data_pin, 0)
  wiringpi2.delay(delay)

# SendInteger
#   Converts an Decimal Value to a command
#   and sends it via SendData
def SendInteger(num):
	if(num < 255):
		binstr = "00" + "{0:b}".format(num)
    	binstr = "0" * (7-(len(binstr)-3)) + binstr
    	SendData(binstr)

# Init
#   Initialized wiringpi 
#   and start Xbox 360 boot sequence.
def Init():
	wiringpi2.pinMode(data_pin, 0)
	wiringpi2.pinMode(clock_pin, 0)
	wiringpi2.wiringPiSetup()
	
	SendData(cmdlist["led_cmd"])
	wiringpi2.delay(50)

# BootAnimation
#    Plays Xbox 360 Boot Animation
def BootAnimation():
	SendData(cmdlist["anim_cmd"])
        wiringpi2.delay(7000)


# SendCommand
#   sends a command according to its name
def SendCommand(name, delay=0):
    	SendData(cmdlist[name],delay)

# Delay
#    Well.. it just forwards the wiringPi delay 
#    function so you don't have to call it from there.
def Delay(ms):
	wiringpi2.delay(ms)

#Brutefore
#    Brutefoce attack
#    ignore_known to false if you want to trigger 
#    commands that are already in cmdlist.
def Bruteforce(begin=0, end=255, ignore_known=True):
  while begin <= end:
	binstr = "00" + "{0:b}".format(begin)
	binstr = "0" * (7-(len(binstr)-3)) + binstr
	if binstr not in cmdlist.values() or ignore_known == False:
		SendData(binstr)
		print(binstr + " : " + str(begin))
	else:
		print(binstr + " : " + cmdlist_reversed[binstr])
	wiringpi2.delay(1000)
	begin += 1
