import paramiko
import sys


def main(port):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('localhost', port=port, username='user', password='pass')
    transport = client.get_transport()
    session = transport.open_session()
    message = "Hello, Paramiko!"
    session.send(message)
    received = session.recv(1024)
    print(f"Server response: {received.decode()}")
    session.close()
    client.close()


if __name__ == '__main__':
    main(sys.argv[1])
