# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from exceptions import Empty
from priority_queue_base import PriorityQueueBase


class SortedPriorityQueue(PriorityQueueBase):  # base class defines _Item
    """A min-oriented priority queue implemented with a sorted list."""

    # ------------------------------ public behaviors ------------------------------
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = []

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""

        # Create a new instance of the _Item class using the provided key and value.
        newest = self._Item(key, value)

        # Loop through the index (i) and the item (item) at each position in the list
        for i, item in enumerate(self._data):
            # Compare the newly created item newest with the current item in the list
            # Since the list is sorted, we look for the first item in the list that is larger than the new item
            if newest < item:

                # Insert the new item at the position (i). This maintains the sorted order of the list.
                self._data.insert(i, newest)

                # After inserting the new item, we break out of the loop because we've found the correct position and completed the insertion
                break
        else:

            # Append if the correct position is at the end
            self._data.append(newest)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        # Raise an exception if the priority queue is empty
        if self.is_empty():
            raise Empty("Priority queue is empty.")

        # Return the smallest item is at the front of the list
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        # Raise an exception if empty if the priority queue is empty
        if self.is_empty():
            raise Empty("Priority queue is empty.")

        # Remove the smallest item from the front of the list
        item = self._data.pop(0)

        # Return the key-value pair of the removed item
        return (item._key, item._value)


# Example usage
if __name__ == "__main__":
    pq = SortedPriorityQueue()
    pq.add(5, "A")
    pq.add(9, "C")
    pq.add(3, "B")
    pq.add(7, "D")

    print("Min:", pq.min())  # Should print (3, 'B')
    print("Remove Min:", pq.remove_min())  # Should remove and print (3, 'B')
    print("Min:", pq.min())  # Should print (5, 'A')
