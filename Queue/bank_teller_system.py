'''
@Author: Shubham shirke
@Date: 2023-06-22 12:08:30
@Last Modified by: Shubham shirke
@Last Modified time: 2023-06-22 13:20:30
@Title : Write a program to simulate a bank teller system where customers arrive in a queue and are served based on priority.
'''

from queue import PriorityQueue
import time

class Customer:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"Customer: {self.name}, Priority: {self.priority}"


def bank_teller_system():
    """
    Description : 
            This is the main function which provides a interface to user for inserting name and priority of the customer and simarly sort the elements and show based on priority. 
    Parameters :
            none
    Returns :
            none
    """
    queue = PriorityQueue()

    while True:
        print("\n1. Add Customer to Queue")
        print("2. Serve Customer")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            name = input("Enter customer name: ")
            priority = int(input("Enter customer priority (1-5): "))
            customer = Customer(name, priority)
            queue.put(customer)
            print(f"Customer {customer.name} added to the queue.")

        elif choice == '2':
            if not queue.empty():
                
                elements = []
                while not queue.empty():
                    elements.append(queue.get())

                sorted_elements = sorted(elements, key=lambda x: x.priority,reverse=True)

                for customer in sorted_elements:
                    print(f"Serving customer: {customer}")
                    time.sleep(1)
                    print(f"Customer {customer.name} served.")

            else:
                print("No customers in the queue.")

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")

# main
def main():
    bank_teller_system()


if __name__ == "__main__":
    main()
