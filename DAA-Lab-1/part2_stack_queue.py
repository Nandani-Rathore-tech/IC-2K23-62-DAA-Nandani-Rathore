# Part 2 - Stack and Queue

tasks = ["Task1", "Task2", "Task3", "Task4", "Task5"]

# Stack
stack = tasks.copy()
stack_order = []

while stack:
    stack_order.append(stack.pop())

# Queue
queue = tasks.copy()
queue_order = []

while queue:
    queue_order.append(queue.pop(0))

print("Stack Order:", stack_order)
print("Queue Order:", queue_order)
print("Printer should use: Queue")