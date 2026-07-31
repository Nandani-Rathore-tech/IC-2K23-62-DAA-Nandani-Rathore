# Lab Task 1

## Part 1 - Trace It Yourself

### Input
8, 3, 15, 6, 2

### Output
Maximum = 15

Sorted List = 2, 3, 6, 8, 15

Comparisons = 4

### Dry Run
- Compare 3 with 8
- Compare 15 with 8 → Max = 15
- Compare 6 with 15
- Compare 2 with 15

Sorting Method: Bubble Sort

Explanation:
The program checks every element once to find the maximum value.
Bubble Sort repeatedly swaps adjacent elements until the list is sorted.

---

## Part 2 - Stack or Queue

Stack Order:
Task5 → Task4 → Task3 → Task2 → Task1

Queue Order:
Task1 → Task2 → Task3 → Task4 → Task5

Printer should use:
Queue (FIFO)

Reason:
A printer prints jobs in the order they arrive, so Queue is the correct data structure.

---

## Part 4 - Count the Steps

Single Loop Runs:
5

Nested Loop Prints:
25

For n = 10

Single Loop = 10

Nested Loop = 100

Explanation:
A single loop grows linearly O(n).
Nested loops grow quadratically O(n²).

---

## How to Run

```bash
python part1_trace.py
python part2_stack_queue.py
python part4_complexity.py
```
