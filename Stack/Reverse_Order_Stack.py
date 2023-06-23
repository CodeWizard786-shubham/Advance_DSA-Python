'''
@Author: Shubham shirke
@Date: 2023-06-21 22:08:30
@Last Modified by: Shubham shirke
@Last Modified time: 2023-06-21 22:08:30
@Title : Given a stack, write a program to reverse the order of its elements using only one additional stack.
'''
from stack_log import logger

class Stack:

    def __init__(self):
        # default constructor
        self.stack_list = []

    def is_empty(self):
        # returns true if stack empty 
        return len(self.stack_list) == 0

    def push(self, item):
        # insert element in to stack
        self.stack_list.append(item)

    def pop(self):
        # remove element from the stack
        if self.is_empty():
            logger.warning("Stack is empty")
        return self.stack_list.pop()

    def reverse_stack(self):
        """
        Description : 
                This function removes the items from original stack and put it into new stack and similarly removes items from the new stack and put it into orignal stack.
                Here the removal from the new stack is done from the top side.
        Parameters :
                self : default constructor.
        Returns :
                self.stack_list : orignal stack with elemetns in the reverse order.
        """
        if self.is_empty():
            return self.stack_list

        new_stack = []
        while not self.is_empty():
            new_stack.append(self.pop())

        while new_stack:
            self.push(new_stack.pop())

        return self.stack_list


def main():
    logger.info("Stack Program started")
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)

    original_stack = stack.reverse_stack()
    print(f"The stack after reverse is: {original_stack}")
    logger.info("Stack Program finished")


if __name__ == "__main__":
    main()
