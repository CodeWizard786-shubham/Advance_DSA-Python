'''
@Author: Shubham shirke
@Date: 2023-06-21 14:02:30
@Last Modified by: Shubham shirke
@Last Modified time: 2023-06-21 14:02:30
@Title : Implement a stack using a linked list and write functions to push, pop, and check if the stack is empty.
'''
from stack_log import logger

class Node:
    def __init__(self, data):
        # default constructor
        self.data = data
        self.next = None

class Stack:
    
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            logger.warning("Stack is empty. Cannot pop.")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

def main():
    logger.info("Stack Program started")
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)

    print(stack.pop()) 
    print(stack.pop())  
    print(stack.pop()) 
    print(stack.pop())  
    print(stack.pop())
    print(stack.pop())
    print(stack.is_empty())
    logger.info("Stack Program Finished")


if __name__ == "__main__":
    main()