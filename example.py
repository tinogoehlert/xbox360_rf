# xbox_rf example script
# 
# Example that shows how to use the
# xbox_rf librabry
#
# Created by Tino Goehlert
# 
# www.astrorats.org | @_tin0_

import xbox_rf

# Initialize wiringPi and start
# Boot secuence.
print("initializing..")
xbox_rf.Init()
xbox_rf.BootAnimation()
print("done")

# Switch Green Edge LEDs on and off
print("start green light travel")
xbox_rf.SendCommand("green_ul",150)
xbox_rf.SendCommand("green_ur",150)
xbox_rf.SendCommand("green_dr",150)
xbox_rf.SendCommand("green_dl",150)
print("done")

# Switch all Green Edge LEDs on
print("full green ON")
xbox_rf.SendData("0010100001",150)
xbox_rf.SendData("0010100011",150)
xbox_rf.SendData("0010101011",150)
xbox_rf.SendData("0010101111",150)
print("done")

# Switch Red Edge LEDs on and off
print("start red light travel")
xbox_rf.SendCommand("red_ul",150)
xbox_rf.SendCommand("red_ur",150)
xbox_rf.SendCommand("red_dr",150)
xbox_rf.SendCommand("red_dl",150)
print("done")

# Switch all Red Edge LEDs on
print("full red ON")
xbox_rf.SendData("0010110001",150)
xbox_rf.SendData("0010110011",150)
xbox_rf.SendData("0010111011",150)
xbox_rf.SendData("0010111111",150)
print("done")

# shotdown all green Edge LEDs on
print("kill green lighting")
xbox_rf.SendData("0010101011",150)
xbox_rf.SendData("0010100111",150)
xbox_rf.SendData("0010100011",150)
xbox_rf.SendData("0010100001",150)
xbox_rf.SendData("0010100000",150)
print("done")

xbox_rf.SendData("0010110000",150)
