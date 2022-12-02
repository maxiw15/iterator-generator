class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor + 1 > len(self.list_of_list):
            raise StopIteration
        element = self.list_of_list[self.cursor]
        if element:
            answer = element.pop(0)
            if not element:
                self.cursor += 1
            return answer
        else:
            self.cursor += 1


def test_1():
    answer = []
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item
        answer.append(flat_iterator_item)
    assert answer == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()


