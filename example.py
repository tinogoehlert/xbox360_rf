# xbox_rf example script
# 
# Example that shows how to use the
# xbox_rf librabry
#
# Created by Tino Goehlert
# 
# www.astrorats.org | @_tin0_

import xbrf

# Initialize wiringPi and start
# Boot secuence.
print("initializing..")
xbrf.Init()
print("done")

# Switch Green Edge LEDs on and off
print("start green light travel")
xbrf.SendCommand("green_ul",150)
xbrf.SendCommand("green_ur",150)
xbrf.SendCommand("green_dr",150)
xbrf.SendCommand("green_dl",150)
print("done")

# Switch all Green Edge LEDs on
print("full green ON")
xbrf.SendData("0010100001",150)
xbrf.SendData("0010100011",150)
xbrf.SendData("0010101011",150)
xbrf.SendData("0010101111",150)
print("done")

# Switch Red Edge LEDs on and off
print("start red light travel")
xbrf.SendCommand("red_ul",150)
xbrf.SendCommand("red_ur",150)
xbrf.SendCommand("red_dr",150)
xbrf.SendCommand("red_dl",150)
print("done")

# Switch all Red Edge LEDs on
print("full red ON")
xbrf.SendData("0010110001",150)
xbrf.SendData("0010110011",150)
xbrf.SendData("0010111011",150)
xbrf.SendData("0010111111",150)
print("done")

# shotdown all green Edge LEDs on
print("kill green lighting")
xbrf.SendData("0010101011",150)
xbrf.SendData("0010100111",150)
xbrf.SendData("0010100011",150)
xbrf.SendData("0010100001",150)
xbrf.SendData("0010100000",150)
print("done")