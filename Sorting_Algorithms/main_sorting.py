'''
@Author: Shubham shirke
@Date: 2023-06-21 11:29:30
@Last Modified by: Shubham shirke
@Last Modified time: 2023-06-21 13:29:30
@Title : Main function to sort list of integers in selection sort or bubble sort or merge sort.
'''

from sort_log import logger

from SortingAlgorithms import selectionSorting,BubbleSorting,MergeSorting

def main():

    try:
        logger.info("Program Started")
        while True:
            print("-- Sorting Algorithms --")
            print("select algorithm to sort: ")
            print("1.Selection sort\n2.Bubble sort\n3.Merge sort\n4.Exit")
            user_choice =int(input("Enter choice: "))
            if user_choice == 4:
                logger.info("Program Finished")
                break
            input_numbers = list(input("Enter numbers seperated by commas: ").split(","))
            array_of_numbers = [eval(num) for num in input_numbers] # list comprehension
            # call selection sort class
            if user_choice == 1:
                select_sort = selectionSorting(array_of_numbers)
                sorted_array = select_sort.sorting_algo()
                select_sort.display_sorted_array(sorted_array)
                input("Hit enter to run again!")
                continue
            # call bubble sort class
            elif user_choice == 2:
                bubble_sort = BubbleSorting(array_of_numbers)
                sorted_array = bubble_sort.sorting_algo()
                bubble_sort.display_sorted_array(sorted_array)
                input("Hit enter to run again!")
                continue
            # call merge sort class
            elif user_choice == 3:
                merge_sort = MergeSorting(array_of_numbers)
                sorted_array = merge_sort.sorting_algo()
                merge_sort.display_sorted_array(sorted_array)
                input("Hit enter to run again!")
                continue

            else:
                logger.warning("Please enter correct option")
                continue


    except Exception as e:
        logger.error(f"Enter integers seperated by commas")
        


# start of Execution
if __name__ == "__main__":
    main()