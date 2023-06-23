'''
@Author: Shubham shirke
@Date: 2023-06-21 21:08:30
@Last Modified by: Shubham shirke
@Last Modified time: 2023-06-21 21:08:30
@Title : Implementing a queue using a linked list and write functions to enqueue, dequeue, and check if the queue is empty.
'''
from queue_log import logger

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

     # constructor   
    def __init__(self):
        self.front = None
        self.rear = None

        # check is empty
    def is_empty(self):
        """
        Description : 
                This function returns if the front of the queue is empty.
        Parameters :
                self
        Returns    :
                self.front is none
        """
        return self.front is None

        # insert into queue
    def enqueue(self, item):
        """
        Description : 
                This function insert a element to the queue from back.
        Parameters  :
                item : element to insert.
        Returns     :
                none
        """
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        # remove from the queue
    def dequeue(self):
        """
        Description :
                This function removes a element from the queue from the front.
        Parameters :
                self : Queue from the constructor
        Returns    :
                front_data : element removed from the front.
        """
        if self.is_empty():
            return None
        front_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return front_data


# main
def main():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())


if __name__ == "__main__":
    main()
