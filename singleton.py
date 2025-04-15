class Dog:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, voice, spices):
        self.voice = voice
        self.spices = spices

    def __del__(self):
        Dog.__instance = None