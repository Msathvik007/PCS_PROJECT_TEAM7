import os
import Pyro4

@Pyro4.expose
class P2PFileServer:
    def __init__(self):
        self.file_storage = {}

    def add_file(self, filename, content):
        if filename in self.file_storage:
            return f"File '{filename}' already exists on the server."
        self.file_storage[filename] = content
        return f"Added file '{filename}' to the server."

    def delete_file(self, filename):
        if filename in self.file_storage:
            del self.file_storage[filename]
            return f"Deleted file '{filename}' from the server."
        else:
            return f"File '{filename}' not found on the server."

    def write_file(self, filename, content):
        self.file_storage[filename] = content
        return f"Updated file '{filename}' on the server."

    def restore_file(self, filename):
        if filename in self.file_storage:
            return self.file_storage[filename]
        else:
            return f"File '{filename}' not found on the server."

def start_server():
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(P2PFileServer)

    ns.register("p2p_server", uri)
    print("P2P Server is ready.")
    daemon.requestLoop()

#startup code 
if __name__ == "__main__":
    start_server()
