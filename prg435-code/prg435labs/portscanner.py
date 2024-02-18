import socket

t = "https://www.hackthissite.org/"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def check_port(port):
    try:
        c = s.connect((t, port))
        return True
    except:
        return False


for a in range(200):
    if check_port(a):
        print("Port", a)
