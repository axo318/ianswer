from typing import List


def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer


class Responsibility:
    d = {}

    @staticmethod
    @parametrized
    def register(subclass, extensions: List[str]):
        for extension in extensions:
            Responsibility.d[extension] = subclass
