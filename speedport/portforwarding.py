class PortForwarding:
    def __init__(self, data):
        self._data = data

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__} ({self.__dict__})"

    def __getitem__(self, item):
        try:
            return self.__getattribute__(item)
        except AttributeError:
            return self._data.get(f"portforward_{item}", self._data.get(item))

    @property
    def data(self):
        return self._data

    @property
    def id(self):
        return self._data.get("portforward_id", "")

    @property
    def name(self):
        return self._data.get("portforward_name", "")

    @property
    def active(self):
        return bool(int(self._data.get("portforward_active", "0")))
