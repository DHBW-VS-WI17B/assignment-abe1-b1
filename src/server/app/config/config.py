class Config:
    # TODO
    __conf = {
        'HOST': '',
        'PORT': '',
        'SQLITE_DATABASE': 'file::memory:?cache=shared',
    }
    __setters = ['host', 'port']

    @staticmethod
    def get(name):
        return Config.__conf[name]

    @staticmethod
    def set(key, value):
        if key in Config.__setters:
            Config.__conf[key] = value
        else:
            raise NameError("Key is invalid.")
