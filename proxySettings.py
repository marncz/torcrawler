import socks
import socket

def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)

# patch the socket module
socket.socket = socks.socksocket
socket.create_connection = create_connection
