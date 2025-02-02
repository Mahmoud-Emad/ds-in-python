# BoundedArrayStack

BoundedArrayStack is a stack data structure implemented using a fixed-size array. It supports basic stack operations such as push, pop, peek, clear, size checking, and capacity management.

## Run the example

To run the example, type `python3 example.py` in the terminal.

## Class Methods

- `push(item)`: Adds an item onto the stack.
- `pop()`: Removes and returns the top item from the stack.
- `peek()`: Returns the top item from the stack without removing it.
- `is_empty()`: Checks if the stack is empty.
- `is_full()`: Checks if the stack is full.
- `size()`: Returns the current number of items in the stack.
- `clear()`: Clears the stack by resetting its state.

## Notes

- The capacity of the stack must be specified during initialization (`BoundedArrayStack(capacity)`).
- Operations such as pushing to a full stack or popping from an empty stack will raise appropriate exceptions (`OverflowError` and `IndexError`, respectively).
