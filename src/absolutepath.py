from pathlib import Path


def absolutepath(filepath):
    relative = Path(filepath)
    print("hello")
    print(relative.absolute())
    return relative.absolute()