import socket

THIS_ADDRESS = ("0.0.0.0", 8000)
UPSTREAM_ADDRESS = ("127.0.0.1", 9000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(THIS_ADDRESS)
s.listen(10)
print(f"Listening on {THIS_ADDRESS}")
