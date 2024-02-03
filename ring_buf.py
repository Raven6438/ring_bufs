class RingBuf:
    def __init__(self, *, max_size):
        self._max_size = self._validate_max_size(max_size)
        self._seq = [None] * max_size
        self._head_pos = 0
        self._tail_pos = 0

    def get_seq(self):
        return self._seq

    @staticmethod
    def _validate_max_size(value):
        if not isinstance(value, int):
            raise MaxSizeIsNotIntError(value)
        if value < 0:
            raise MaxSizeIsNotPositiveError()
        return value

    def _is_full(self):
        return None not in self.get_seq()

    def _increment_head_pos(self):
        self._head_pos = new_head_pos if (new_head_pos := self._head_pos + 1) < self._max_size else 0

    def _increment_tail_pos(self):
        self._tail_pos = new_tail_pos if (new_tail_pos := self._tail_pos + 1) < self._max_size else 0

    def push(self, item):
        seq = self.get_seq()

        if self._is_full():
            seq[self._head_pos] = item
            self._increment_head_pos()
            self._increment_tail_pos()
        else:
            seq[self._tail_pos] = item
            if seq[0] is not None:
                self._increment_tail_pos()

    def pop(self):
        seq = self.get_seq()
        seq[self._head_pos] = None
        self._increment_head_pos()

    def clear(self):
        seq = self.get_seq()
        for i in range(self._max_size):
            seq[i] = None

        self._head_pos = 0
        self._tail_pos = 0


class MaxSizeIsNotIntError(Exception):
    def __init__(self, max_size: int, msg: str = None):
        self.max_size = max_size
        self.msg = msg or f'Max size value must be an int type! But is a {type(self.max_size)} '
        super().__init__(self.msg)


class MaxSizeIsNotPositiveError(Exception):
    def __init__(self, msg: str = None):
        self.msg = msg or 'Значение max_size должно быть положительным числом!'
        super().__init__(self.msg)
