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
            raise Exception('Значение должно быть числом!')
        if value < 0:
            raise Exception('Значение max_size должно быть положительным числом!')
        return value

    def _is_full(self):
        return None not in self.get_seq()

    def increment_head_pos(self):
        self._head_pos = new_head_pos if (new_head_pos := self._head_pos + 1) < self._max_size else 0

    def increment_tail_pos(self):
        self._tail_pos = new_tail_pos if (new_tail_pos := self._tail_pos + 1) < self._max_size else 0

    def push(self, item):
        seq = self.get_seq()

        if self._is_full():
            seq[self._head_pos] = item
            self.increment_head_pos()
            self.increment_tail_pos()
        else:
            seq[self._tail_pos] = item
            if seq[0] is not None:
                self.increment_tail_pos()

    def pop(self):
        seq = self.get_seq()
        seq[self._head_pos] = None
        self.increment_head_pos()

    def clear(self):
        seq = self.get_seq()
        for i in range(self._max_size):
            seq[i] = None

        self._head_pos = 0
        self._tail_pos = 0
