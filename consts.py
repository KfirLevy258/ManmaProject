class ArrayConsts:
    MIN_DEFAULT_VALUE = 0
    MAX_DEFAULT_VALUE = 999


class MamanException(Exception):
    def __init__(self, msg: str):
        super(MamanException, self).__init__(msg)
