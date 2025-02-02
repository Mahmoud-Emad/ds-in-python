from stack import BoundedArrayStack


def main():
    # Create a stack with a capacity of 5
    stack = BoundedArrayStack(5)

    # Push elements onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack after pushes:", stack)  # Should print: BoundedArrayStack([10, 20, 30])

    # Peek at the top element
    print("Top element:", stack.peek())  # Should print: 30

    # Pop an element
    print("Popped element:", stack.pop())  # Should print: 30

    # Check stack size
    print("Stack size:", stack.size())  # Should print: 2

    # Check if the stack is empty
    print("Is stack empty?", stack.is_empty())  # Should print: False

    # Push more elements
    stack.push(40)
    stack.push(50)
    stack.push(60)

    print("Stack after more pushes:", stack)  # Should print: BoundedArrayStack([10, 20, 40, 50, 60])

    # Try pushing when stack is full (should raise OverflowError)
    try:
        stack.push(70)
    except OverflowError as e:
        print("Error:", e)  # Should print "Stack is full"

    # Clear the stack
    stack.clear()
    print("Stack after clearing:", stack)  # Should print: BoundedArrayStack([])

    # Try popping from empty stack (should raise IndexError)
    try:
        stack.pop()
    except IndexError as e:
        print("Error:", e)  # Should print "Stack is empty"

if __name__ == "__main__":
    main() 