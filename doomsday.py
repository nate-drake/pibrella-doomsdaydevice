#!/usr/bin/env python

# This variable helps the script decide when the countdown is over
countdownover = 0

import pibrella
import os
import subprocess
import sys
import smtplib
from threading import Timer

# Once countdown reaches zero the 'activate' process begins.

def activate():
    global countdownover
    countdownover = 1
    pibrella.buzzer.off()
    print "Countdown is over"

#Uncomment the lines below to send Doomsday e-mail

#    doomsdaymail()
#    return

#Uncomment the lines below to securely delete files

#    doomsdaydelete()
#    return

####DOOMSDAY SCRIPTS#####

### Doomsday e-mail

#def doomsdaymail():

#    print "Sending Doomsday e-mail..."

#Define server settings

#    server = smtplib.SMTP('smtp.gmail.com', 587) 

# Define sender and receiver e-mail address 

#    sender = 'youremaile@address.com'
#    receiver = ['receiversemail@address.com']

#Now log in to your mail server. Change the e-mail address and password
#according to your account settings. You may want to have a dedicated e-mail
# address for this.

#Request TLS connection

#    server.ehlo()
#    server.starttls()
#    server.ehlo() 

#Login details:

#    server.login("youremail@address.com", "password123")"

#    #Send the message

#    msg = "The Doomsday Switch has been tripped! Send me an emergency donut!"
#    server.sendmail(sender, receiver, msg)
#    print "Closing connection..." 
#    server.close()

#If e-mail is sent successfully, the buzzer will make the 'success' sound.

#    pibrella.buzzer.success()

### End of Doomsday e-mail


### Start Doomsday Delete

#def doomsdaydelete():
	
#    print "Attempting to delete files..."

#Delete a folder securely including its contents
#The file is overwritten 38 times. Last pass is all zeroes.

#    folderpath = "/home/pi/Documents/private"
#    subprocess.call(["srm", "-rvz", folderpath])

#Delete a file securely using 'shred'
#The file is overwritten 25 times. Last pass is all zeroes.

#    filepath = "/home/pi/Documents/secretfile1.txt"
#    subprocess.call(["shred", "-zu", filepath])
#    print "Files have been shredded."
#If files are deleted, the buzzer will make the 'success' sound.

#    pibrella.buzzer.success()

### End Doomsday Delete


####END OF DOOMSDAY SCRIPTS####
    



# Define countdown parameters. By default this is 10.0 seconds.

t = Timer(10.0, activate)

# Start the countdown
t.start()

#If the red button is pressed during the countdown, the program will exit.

while countdownover ==0:
		pibrella.buzzer.note(2)
		pibrella.light.red.blink(1, 1)		
		if pibrella.button.read() == 1:
				t.cancel()
				sys.exit()


#Once the countdown is complete, the Red LED stops blinking but remains on.

while countdownover ==1:
	pibrella.light.red.on()
