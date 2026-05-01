import socket
import paramiko
import threading
import sys


HOST_KEY = '/etc/ssl/private/server.key'


class EchoServerInterface(paramiko.ServerInterface):
    def check_auth_password(self, username, password):
        return paramiko.OPEN_SUCCEEDED

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED


def handle_connection(client_socket):
    transport = paramiko.Transport(client_socket)
    hostkey = paramiko.RSAKey(filename=HOST_KEY)
    transport.add_server_key(hostkey)
    server = EchoServerInterface()
    transport.start_server(server=server)
    chan = transport.accept()
    if chan is None:
        return
    print(f"Connected: {transport.getpeername()}")
    while True:
        data = chan.recv(1024)
        if not data:
            break
        print(f"Received: {data.decode()}")
        chan.send(b"Echo: " + data)
    chan.close()


def main(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', port))
    sock.listen(100)
    print(f"Listening on port {port}...")
    while True:
        client, _ = sock.accept()
        threading.Thread(target=handle_connection, args=(client,)).start()


if __name__ == '__main__':
    main(int(sys.argv[1]))
