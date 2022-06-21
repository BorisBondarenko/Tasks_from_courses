from random import sample


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


class Router:

    def __init__(self):
        self.buffer = []
        self.servers = []

    def link(self, server):
        server.linked_router = self
        if server not in self.servers:
            self.servers.append(server)

    def unlink(self, server):
        if server in self.servers:
            server.linked_router = None
            self.servers.remove(server)

    def send_data(self):
        for data in self.buffer:
            for server in self.servers:
                if server.get_ip() == data.ip:
                    server.buffer.append(data)
                else:
                    continue

        self.buffer = []


class Server:

    def __init__(self):
        self.buffer = []
        self.linked_router = None
        self.ip = '.'.join(map(str, sample(range(0, 225), 4)))

    def send_data(self, data):
        if self.linked_router:
            self.linked_router.buffer.append(data)

    def get_data(self):
        res = self.buffer[:]
        self.buffer.clear()
        return res

    def get_ip(self):
        return self.ip
