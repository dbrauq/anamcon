# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from socket import (socket as _socket, 
                    AF_INET, 
                    SOCK_STREAM)

def is_available_port(port):
    try:
        socket = _socket(AF_INET, SOCK_STREAM)
        socket.bind(("localhost", port))
        return True
    except:
        return False

def get_available_ports(min_port_number=0, max_port_number=65535):
    available_ports=[]
    for port in range(min_port_number,max_port_number+1, 1):
        if is_available_port(port):
            available_ports.append(port)
    return available_ports
