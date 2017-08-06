# pibrella-doomsdaydevice
Turn your Raspberry Pi into a handy Doomsday device using the Pibrella board and these handy Python scripts

The Pibrella board (http://pibrella.com/) represents one of the easiest way to play with electronics on your Raspberry Pi. It comes complete with a big red button, three coloured LEDs and a small buzzer as well as numerous I/O interfaces. 

For this project, I have created some python scripts to turn your Pi+Pibrella into your very own "Doomsday Device". 

The first script 'isconnected.py' runs on a continuous loop and simply checks that your Pi can connect to the internet via trying to resolve a domain name (by default this is http://google.com). If successful the green LED will blink once every second. 

The second script 'primed.py' also runs continuously, monitoring whether the button on the Pibrella board has been pressed. If so it will launched the third script 'doomsday.py'. While 'primed.py' is running it illuminates the yellow LED on the Pibrella board, so that you can be sure your Doomsday switch is primed. 

The 'doomsday.py' script by default will begin a 10 second countdown when pressed. During this time the buzzer will sound and the red LED will blink once every second. You can press the red button again to disarm the Doomsday switch and exit the script. 

As it stands, the 'doomsday.py' script will simply illuminate the red LED steadily once it executes. There are however two functions contained in the script which you can uncomment and configure either to send an e-mail to a certain address with the text of your choice, or to securely delete files on the Pi. 

Questions/Comments please contact me via my website http://www.natewriter.com
