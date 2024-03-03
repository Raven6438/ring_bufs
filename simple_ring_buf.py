import exceptions


class SimpleRingBuf:
    def __init__(self, *, max_size):
        self._max_size = self._validate_max_size(max_size)
        self._seq = []
        self._head_pos = 0

    @staticmethod
    def _validate_max_size(value):
        if not isinstance(value, int):
            raise exceptions.MaxSizeIsNotIntError(value)
        if value < 0:
            raise exceptions.MaxSizeIsNotPositiveError()
        return value

    def get_seq(self):
        return self._seq

    def get_head_pos(self):
        return self._head_pos

    def _is_full(self):
        return len(self._seq) == self._max_size

    def _increment_head_pos(self):
        self._head_pos = new_head_pos if (new_head_pos := self._head_pos + 1) < self._max_size else 0

    def push_item(self, item):
        seq = self.get_seq()
        if self._is_full():
            seq[self._head_pos] = item
            self._increment_head_pos()
        else:
            seq.append(item)

    def push_items(self, *args, **kwargs):
        for item in args:
            self.push_item(item)

    def pop(self):
        seq = self.get_seq()
        del seq[self._head_pos]

    def get_item_by_index(self, index):
        if index >= self._max_size:
            raise IndexError('Индекс превысил размер буфера!')

        seq = self.get_seq()
        try:
            return seq[index]
        except IndexError:
            return None

    def clear(self):
        seq = self.get_seq()
        seq.clear()
        self._head_pos = 0
