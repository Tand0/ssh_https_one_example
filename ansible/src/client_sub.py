import paramiko
import sys


def main(ip, port):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username='t-ando', password='t-ando')
    transport = client.get_transport()
    channel = transport.open_session()
    channel.invoke_subsystem("echo-subsystem")
    message = "Hello, Paramiko!\r\n"
    channel.sendall(message)
    print(f"Sent: {message}")
    print(f"Received: {channel.recv(1024).decode()}")

    channel.close()
    client.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
