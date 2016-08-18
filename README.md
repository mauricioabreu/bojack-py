# BoJack client written in Python

A Python interface to the [BoJack](https://github.com/marceloboeira/bojack) in-memory key value store.

## Installation

Python 3.4+

```
pip install bojack-py
```

## Usage

```python
>>> from bojack.client import Client

>>> client = Client('127.0.0.1', 5000)
>>> client.set('foo', 'bar')
b'bar'
>>> client.get('foo')
b'bar'
```

## Contributing

Found a bug? Have a suggestion? Please [open an issue](https://github.com/mauricioabreu/bojack-py/issues/new).

Want to contribute? Make sure you follow the [guide](https://github.com/mauricioabreu/bojack-py/blob/master/CONTRIBUTING.md).
