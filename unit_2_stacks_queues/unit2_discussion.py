"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        self.items = []
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        

    def push(self, value):
        # The newest value goes on top of the stacl (LIFO)
        self.items.append(value)
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        

    def peek(self):
        # View the top item without removing it.
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        

    def is_empty(self):
        return len(self.items) == 0
        # TODO (Student): Return True if the stack has no values.
        


class Queue:
    def __init__(self):
        self.items = deque()
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        

    def enqueue(self, value):
        # New items join the back of the queue (FIFO)
        self.items.append(value)
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.popleft()
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        

    def front(self):
        # View thr first item without removing it.
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        

    def is_empty(self):
        return len(self.items) == 0
        # TODO (Student): Return True if the queue has no values.
        


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    print("\n=== STACK DEMO ===")
    stack = Stack()

    for value in [10, 20, 30, 40]:
        stack.push(value)
        print("Added to stack:", value)

    print("Top item:", stack.peek())
    print("Removing items (LIFO):")

    while not stack.is_empty():
        print(stack.pop())

    print("Pop from empty stack:", stack.pop())
    print("Peek at empty stack:", stack.peek())

    single_stack = Stack()
    single_stack.push(50)
    print("Single item removed:", single_stack.pop())
    print("Is stack empty?", single_stack.is_empty())

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")
queue = Queue()

for value in [10, 20, 30, 40]:
    queue.enqueue(value)
    print("Added to queue:", value)

print("Front item:", queue.front())
print("Removing items (FIFO):")

while not queue.is_empty():
    print(queue.dequeue())

print("Dequeue from empty queue:", queue.dequeue())
print("Front of empty queue:", queue.front())

single_queue = Queue()
single_queue.enqueue(50)
print("Single item removed:", single_queue.dequeue())
print("Is queue empty?", single_queue.is_empty())

print("\n=== REAL-WORLD EXAMPLE ===")
support_queue = Queue()

support_queue.enqueue("Password reset")
support_queue.enqueue("Printer issue")
support_queue.enqueue("Software update")

print("First customer helped:", support_queue.dequeue())
print("Next customer:", support_queue.front())

if __name__ == "__main__":
    main()
