import socket
import sys


def main(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
        s.listen()
        while True:
            print(f'Server listening on {port}')
            try:
                conn, addr = s.accept()
                with conn:
                    print(f'Connected by {addr}')
                    data = conn.recv(1024)
                    if data:
                        result = f"Echo: {data.decode()}\n"
                        conn.sendall(result.encode())
            finally:
                pass


if __name__ == '__main__':
    main(int(sys.argv[1]))
