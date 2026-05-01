import paramiko
import sys


def main(ip, port, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=username, password=password)
    transport = client.get_transport()
    session = transport.open_session()
    message = "Hello, Paramiko!"
    session.send(message)
    received = session.recv(1024)
    print(f"Server response: {received.decode()}")
    session.close()
    client.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
