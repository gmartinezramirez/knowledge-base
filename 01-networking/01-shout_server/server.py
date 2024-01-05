"""
Objetive: understand four important socket-related system calks
 - socket
 - bind
 - recvfrom
 - sendto
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 0.0.0.0 is ip address 

s.bind(('0.0.0.0', 9999))

while True:
  msg, sender = s.recvfrom(4096)
  print(f'Recieved {msg.decode("utf8")} from {sender}')

