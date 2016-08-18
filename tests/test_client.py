from bojack.client import Client


class TestClient:

    @classmethod
    def setup_class(cls):
        cls.client = Client('127.0.0.1', 5000)

    def test_set(self):
        result = self.client.set('foo', 'bar')
        assert result == b'bar'

    def test_get(self):
        result = self.client.get('foo')
        assert result == b'bar'

    def test_delete(self):
        result = self.client.delete('foo')
        assert result == b'bar'

    def test_append(self):
        self.client.set('list', 'foo,bar')
        result = self.client.append('list', 'lol')
        assert result == b'["foo", "bar", "lol"]'

    def test_pop(self):
        result = self.client.pop('list')
        assert result == b'lol'

    def test_size(self):
        result = self.client.size()
        assert result == b'1'

    def test_ping(self):
        result = self.client.ping()
        assert result == b'pong'
