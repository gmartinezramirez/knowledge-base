"""
goal: write a simple http server which serves back the request header as JSON
this uses HTTP/1.1
subgoals:
    - parse http request
    - format headers in JSON
    - send response
"""

import json
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 7777))

s.listen()
print("Listening new connections on port 7777")

while True:
    # connection is a socket object
    connection, address = s.accept()
    print(f"New connection from {address}")
    # 4096 is the buffer size
    req = connection.recv(4096)
    headers, body = req.split(b"\r\n\r\n")
    d = {}
    for line in headers.split(b"\r\n")[1:]:
        key, value = line.split(b":")
        d[key.decode("ascii")] = value.decode("ascii")

    connection.send(b"HTTP/1.1 200 OK\r\n")
    connection.send(json.dumps(d, indent=2).encode("ascii"))
    connection.close()
