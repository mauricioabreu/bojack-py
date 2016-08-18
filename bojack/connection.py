import socket


class Socket:

    def __init__(self, hostname, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((hostname, port))

    def puts(self, command):
        """Send a command to the socket.

        :param command: a BoJack command.
        :type: str
        :rtype: bytes
        """
        self.socket.sendall(bytes(command + '\n', encoding='utf-8'))
        return command

    def gets(self):
        """Receive data from the socket.

        Iterates the response in chunks until it finds
        a newline terminator.

        :rtype: bytes
        """
        data = b''
        while True:
            data += self.socket.recv(1024)
            if data.endswith(b'\n'):
                break
        return data.strip()
