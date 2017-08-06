#!/usr/bin/env python

import urllib2

import pibrella

import socket
REMOTE_SERVER = "www.google.com"
def is_connected():
  try:
    # This part checks if the  host name can be resolved.
    host = socket.gethostbyname(REMOTE_SERVER)
    # The above line actually attempts to  connect to the host
    # and let's us know if the address can be reached.
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False

# This sections run the Python script in a continuous loop.
# While the host name can be resolved the green light will blink. 
while is_connected() == True:
	pibrella.light.green.blink(1, 1)
