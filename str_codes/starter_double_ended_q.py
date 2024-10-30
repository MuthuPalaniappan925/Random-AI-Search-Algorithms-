##What is deque? -> It is a doubled ended queue. It is a list-like container with fast appends and pops on either end.
'''We will use this to implement stack and queues'''
from collections import deque

##Let's create a queue -> First Out (FIFO)
queue = deque()
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue after enqueuing A, B, C:", list(queue))

dequeued_element = queue.popleft()  
print("Dequeued element:", dequeued_element)
print("Queue after dequeue:", list(queue))

front_element = queue[0] if queue else None
print("Front element:", front_element)

##Let's create a stack -> Last In (LIFO)
stack = deque()
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack after pushing A, B, C:", list(stack))

popped_element = stack.pop()
print("Popped element:", popped_element)
print("Stack after pop:", list(stack))

top_element = stack[-1] if stack else None
print("Top element:", top_element)