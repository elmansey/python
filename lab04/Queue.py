class Queue:
    # class-level variable to keep track of all queue instances
    _all_queues = {}

    def __init__(self, name, size):
        self._name = name
        self._size = size
        self._queue = []

        # register the new instance to the class-level variable
        self._all_queues[name] = self

    def insert(self, value):
        if len(self._queue) < self._size:
            self._queue.append(value)
        else:
            raise QueueOutOfRangeException(f"Queue '{self._name}' is full")

    def pop(self):
        if not self.is_empty():
            return self._queue.pop(0)
        else:
            print(f"Warning: Queue '{self._name}' is empty")
            return None

    def is_empty(self):
        return len(self._queue) == 0

    @classmethod
    def get_queue_by_name(cls, name):
        return cls._all_queues.get(name)


class QueueOutOfRangeException(Exception):
    pass



# create a new queue instance
q1 = Queue('q1', 2)

# insert values to the queue
q1.insert(1)
q1.insert(2)

try:
    q1.insert(3)
except QueueOutOfRangeException as e:
    print(str(e))  

print(q1.pop())  
print(q1.pop())  
print(q1.pop())  

q2 = Queue('q2', 1)
q1 = Queue.get_queue_by_name('q1')
# print(q1)

# insert values to the queues
# q1.insert(1)
q2.insert(2)

# print(q1.pop())  
print(q2.pop())  