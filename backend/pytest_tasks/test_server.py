import pytest


class Server:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False


@pytest.fixture
def server():
    s = Server()
    s.start()
    yield s
    s.stop()

def test_server_is_running(server):
    assert server.running == True
