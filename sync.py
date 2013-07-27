# xbox_rf sync script
# 
# Example that shows how to use the
# xbox_rf librabry
#
# Created by Tino Goehlert
# 
# www.astrorats.org | @_tin0_

import xbox_rf.py

# start the sync routine
print("start syncing..")
xbrf.SendCommand("ctl_sync",200)
print("done, please press the sync button on your controller")
