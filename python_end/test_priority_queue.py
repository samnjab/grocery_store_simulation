""" Module Description:
This module will contain tests for class PriorityQueue.
"""
import unittest

from container import PriorityQueue


class TestPriorityQueue():
    def test_empty_is_empty(self) -> None:
        pq = PriorityQueue()
        assert pq.is_empty() is True

    def test_non_empty_is_not_empty(self) -> None:
        pq = PriorityQueue()
        pq.add('test')
        assert pq.is_empty() is False

    def test_add_to_empty_priority_queue(self) -> None:
        pq = PriorityQueue()
        pq.add('test')
        assert pq._items == ['test']

    def test_add_in_order_priority_queue(self) -> None:
        pq = PriorityQueue()
        pq.add('test')
        pq.add('test2')
        assert pq._items == ['test', 'test2']

    def test_add_shuffled_priority_queue(self) -> None:
        pq = PriorityQueue()
        pq.add('test2')
        pq.add('test1')
        assert pq._items == ['test1', 'test2']

    def test_add_equal_elements_priority_queue(self) -> None:
        pq = PriorityQueue()
        pq.add('test')
        pq.add('test')
        assert pq._items == ['test', 'test']

    def test_add_to_middle_priority_queue(self) -> None:
        pq = PriorityQueue()
        pq.add('test1')
        pq.add('test3')
        pq.add('test2')
        assert pq._items == ['test1', 'test2', 'test3']

    def test_remove_return_priority_queue(self) -> None:
        pq = PriorityQueue()
        pq.add(1)
        pq.add(2)
        pq.add(0.9)
        assert pq.remove() == 0.9

    def test_remove_priority_queue(self) -> None:
        pq = PriorityQueue()
        pq.add(1)
        pq.add(2)
        pq.add(0.9)
        pq.remove()
        assert pq._items == [1, 2]


if __name__ == '__main__':
    import pytest

    pytest.main(['test_priority_queue.py'])
