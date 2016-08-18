from bojack.client import Client


class TestClient:

    @classmethod
    def setup_class(cls):
        cls.client = Client('127.0.0.1', 5000)

    def test_set(self):
        result = self.client.set('foo', 'bar')
        assert result == 'bar'

    def test_get(self):
        result = self.client.get('foo')
        assert result == 'bar'

    def test_delete(self):
        result = self.client.delete('foo')
        assert result == 'bar'

    def test_append(self):
        self.client.set('list', 'foo,bar')
        result = self.client.append('list', 'lol')
        assert result == '["foo", "bar", "lol"]'

    def test_pop(self):
        result = self.client.pop('list')
        assert result == 'lol'

    def test_size(self):
        result = self.client.size()
        assert result == '1'

    def test_ping(self):
        result = self.client.ping()
        assert result == 'pong'
