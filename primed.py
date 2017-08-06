#!/usr/bin/env python


# The below variable 'doomsday' simply makes sure that the doomsday script
# is only launched once per session when you press the red button.
global doomsday
doomsday = 0

import pibrella
import os

while True:
# If the red button is pressed for first time this session,
#  activate Doomsday script then quit:
         if pibrella.button.read() == 1 and doomsday <>1:
	     os.system('python /home/pi/doomsday.py')
	     print "Doomsday script launched." 
	     doomsday = 1

#If the red  button has not been pressed, wait and keep the yellow LED on:
       	 if pibrella.button.read() == 0:
	     pibrella.light.yellow.on()
