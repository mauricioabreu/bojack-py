from bojack.client import Client


class TestClient:

    @classmethod
    def setup_class(cls):
        cls.client = Client('127.0.0.1', 5000)

    def test_set(self):
        result = self.client.set('foo', 'bar')
        assert result == b'bar'

    def test_get(self):
        self.client.set('foo', 'bar')
        result = self.client.get('foo')
        assert result == b'bar'

    def test_delete(self):
        self.client.set('foo', 'bar')
        result = self.client.delete('foo')
        assert result == b'bar'

    def test_append(self):
        self.client.set('list', 'foo,bar')
        result = self.client.append('list', 'lol')
        assert result == b'["foo", "bar", "lol"]'

    def test_pop(self):
        self.client.set('list', 'foo,bar,lol')
        result = self.client.pop('list')
        assert result == b'lol'

    def test_increment(self):
        self.client.set('counter', 1)
        result = self.client.increment('counter')
        assert result == b'2'

    def test_ping(self):
        result = self.client.ping()
        assert result == b'pong'

    def test_size(self):
        self.client.set('foo', 'bar')
        result = self.client.size()
        assert result == b'1'

    def teardown_method(self, method):
        self.client.delete('*')
