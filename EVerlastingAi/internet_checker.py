import socket

def check_internet_connection():

    IPaddress=socket.gethostbyname(socket.gethostname())
    if IPaddress=="127.0.0.1":
        return False
    else:
        return True

check_internet_connection()
