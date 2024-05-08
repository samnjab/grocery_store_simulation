from __future__ import annotations
from typing import Any


class Container:
    """A container that holds objects.

    This is an abstract class. Only child classes should be instantiated.
    """

    def add(self, item: Any) -> None:
        """Add <item> to this Container.
        """
        raise NotImplementedError

    def remove(self) -> None:
        """Remove and return a single item from this Container.
        """
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Return True iff this Container is empty.
        """
        raise NotImplementedError


class PriorityQueue(Container):
    """A queue of items that operates in priority order.

    Items are removed from the queue according to priority; the item with the
    highest priority is removed first. Ties are resolved in FIFO order,
    meaning the item which was inserted *earlier* is the first one to be
    removed.

    If x < y, then x has a *HIGHER* priority than y.

    Attributes:
    - _items: The items stored in the priority queue. The highest priority item
              is at index 0.

    Representation Invariants:
    - self._items == sorted(self._items, reverse=True)
    - all objects in self._items can be compared to each other using
      comparison operators
    """
    _items: list

    def __init__(self) -> None:
        """Initialize an empty PriorityQueue.
        """
        self._items = []

    def __str__(self) -> str:
        """Return a string representation of the PriorityQueue"""
        str_rep = ''
        for event in self._items:
            str_rep += str(event) + '\n'
        return str_rep

    def remove(self) -> Any:
        """Remove and return the next item from this PriorityQueue.

        Precondition:
        - not self.is_empty()

        >>> pq = PriorityQueue()
        >>> pq.add('fred')
        >>> pq.add('anna')
        >>> pq.add('mona')
        >>> pq.add('hat')
        >>> pq.remove()
        'anna'
        >>> pq.remove()
        'fred'
        >>> pq.remove()
        'hat'
        >>> pq.remove()
        'mona'
        """
        return self._items.pop(0)

    def is_empty(self) -> bool:
        """
        Return True iff this PriorityQueue is empty.

        >>> pq = PriorityQueue()
        >>> pq.is_empty()
        True
        >>> pq.add('fred')
        >>> pq.is_empty()
        False
        """
        return len(self._items) == 0

    def add(self, item: Any) -> None:
        """Add <item> to this PriorityQueue.

        >>> pq = PriorityQueue()
        >>> pq.add('fred')
        >>> pq.add('anna')
        >>> pq.add('sophia')
        >>> pq.add('mona')
        >>> pq._items
        ['anna', 'fred', 'mona', 'sophia']
        """
        if self.is_empty():
            self._items.append(item)
        else:
            added = False
            i = 0
            while not added and i < len(self._items):
                if item < self._items[i]:
                    self._items.insert(i, item)
                    added = True
                i += 1
            if not added:
                self._items.append(item)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
