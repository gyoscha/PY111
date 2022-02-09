"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any

# Очередь основана на списке Питона
# Начало справа, конец слева
# ToDo Сделать вторую реализацию этой очереди (в лекции есть картинка) и peek в обоих случаях


class PriorityQueue:
    def __init__(self):
        self.priority_queue = []

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        enqueue_item = {
            'elem': elem,
            'priority': priority
        }
        if not self.priority_queue:
            self.priority_queue.append(enqueue_item)
            return None

        for index, current_item in enumerate(self.priority_queue):
            if current_item['priority'] <= enqueue_item['priority']:
                self.priority_queue. insert(index, enqueue_item)
                break
        else:   # Если прошли всю очередь и дошли до конца, то добавляем в самое начало.
            self.priority_queue.append(enqueue_item)

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        if not self.priority_queue:
            return None

        return self.priority_queue.pop()['elem']   # O(1)

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        return None

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.priority_queue.clear()
