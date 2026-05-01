import socket
import paramiko
import threading
import sys
import time

HOST_KEY = '/etc/ssl/private/server.key'


class EchoServerInterface(paramiko.ServerInterface):
    def check_auth_password(self, username, password):
        return paramiko.OPEN_SUCCEEDED

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED

    def check_subsystem_request(self, channel, name):
        print(f"check_subsystem_request name={name}")
        return False


class EchoSubsystemHandler(paramiko.server.SubsystemHandler):
    def __init__(self, channel, name, server):
        super().__init__(channel, name, server)
        print("EchoSubsystemHandler")
        self.channel = channel

    def _run(self):
        print("EchoSubsystemHandler _run")
        while True:
            # クライアントからのデータを受信
            data = self.channel.recv(1024)
            if not data or data.decode().strip() == "exit":
                break
            self.channel.sendall(f"Echo: {data.decode()}")
        self.channel.close()


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
    transport.set_subsystem_handler("echo-subsystem", EchoSubsystemHandler)
    try:
        while transport is not None and transport.is_active():
            time.sleep(1)
    finally:
        pass
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
