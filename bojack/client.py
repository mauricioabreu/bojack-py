"""BoJack client written in Python.

"""

from bojack.connection import Socket


class Client:
    """Implementation of BoJack commands.

    It exposes the commands as methods. To see a complete
    list of the available commands read this link:
    https://github.com/marceloboeira/bojack#usage
    """

    def __init__(self, hostname, port):
        self.socket = Socket(hostname, port)

    def set(self, key, value):
        command = 'set {key} {value}'.format(key=key, value=value)
        self.socket.puts(command)
        return self.socket.gets()

    def get(self, key):
        command = 'get {key}'.format(key=key)
        self.socket.puts(command)
        return self.socket.gets()

    def delete(self, key):
        command = 'delete {key}'.format(key=key)
        self.socket.puts(command)
        return self.socket.gets()

    def append(self, key, value):
        command = 'append {key} {value}'.format(key=key, value=value)
        self.socket.puts(command)
        return self.socket.gets()

    def pop(self, key):
        command = 'pop {key}'.format(key=key)
        self.socket.puts(command)
        return self.socket.gets()

    def increment(self, key):
        command = 'increment {key}'.format(key=key)
        self.socket.puts(command)
        return self.socket.gets()

    def size(self):
        self.socket.puts('size')
        return self.socket.gets()

    def ping(self):
        self.socket.puts('ping')
        return self.socket.gets()
