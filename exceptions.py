class MaxSizeIsNotIntError(Exception):
    def __init__(self, max_size: int, msg: str = None):
        self.max_size = max_size
        self.msg = msg or f'Max size value must be an int type! But is a {type(self.max_size)} '
        super().__init__(self.msg)


class MaxSizeIsNotPositiveError(Exception):
    def __init__(self, msg: str = None):
        self.msg = msg or 'Значение max_size должно быть положительным числом!'
        super().__init__(self.msg)
