'''
@Author: Shubham shirke
@Date: 2023-06-21 21:08:30
@Last Modified by: Shubham shirke
@Last Modified time: 2023-06-21 21:08:30
@Title : Given a queue, write a program to reverse the order of its elements using only one additional queue.
'''

from queue_log import logger

class Queue:

    def __init__(self) -> None:
        # ddefault constructor
        self.queue_list = []
        self.new_queue = []


    def size(self):
        # returns the size of the original queue
        return len(self.queue_list)
    
    def is_empty(self):
        # checks if the size of the queue is 0 or not
        if self.size == 0:
            return True    

    def enqueue(self,item):
        # inserts element into the queue
        self.queue_list.append(item)

    def dequeue(self,index):
        # removes an element from the queue
        if self.queue_list == self.is_empty():
            logger.warning("Queue is Empty")
            return None
        else:
            self.queue_list.pop(index)

    def reverse_queue(self):
        """
        Description : 
                This function removes the items from original queue and put it into new queue and similarly removes items from the new queue and put it into orignal queue.
                Here the removal from the new queue is done from the rear side.
        Parameters :
                self : default constructor containg both the queue_list and new_queue.
        Returns :
                self.queue_list : orignal queue with elemetns in the reverse order.
        """
        try:
            if self.size() <= 1:
                return self.queue_list

            while self.queue_list:
                self.new_queue.append(self.queue_list.pop(0))

            while self.new_queue:
                self.queue_list.append(self.new_queue.pop(-1))

            return self.queue_list
        except Exception as e:
            logger.error(str(e))

# main
def main():
    queue = Queue()
    logger.info("Queue Program started")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)


    result = queue.reverse_queue()
    print(f"The reverse of the queue is: {result}")
    logger.info("Queue Program finished")


if __name__ == "__main__":
    main()