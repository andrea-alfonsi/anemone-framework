from pathlib import Path


class SerializableMixin:
    def save(self, path: Path):
        pass

    def load(self, path: Path):
        pass
