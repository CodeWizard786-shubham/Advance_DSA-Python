'''
@Author: Shubham shirke
@Date: 2023-06-20 21:10:30
@Last Modified by: Shubham shirke
@Last Modified time: 2023-06-21 13:29:30
@Title : Implementing the sort algorithms to sort an array of integers in ascending order.
'''

from sort_log import logger
from abc import ABC , abstractmethod

# implement abstraction
class Sorting(ABC):

    @abstractmethod
    def sorting_algo(self):
        pass

    @abstractmethod
    def display_sorted_array(self):
        pass


# selection sort
class selectionSorting(Sorting):

    def __init__(self,array_of_numbers) -> None:
        self.array=array_of_numbers

    def sorting_algo(self):
        try:
            """
            Description : 
                    This function sorts number from the list using selection sort algo.
            Parameters :
                    self : To get list of user input numbers declared in constructor.
            Returns    :
                    array : sorted list of numbers.
            """
            size = len(self.array)

            if size > 0:

                for step in range(size):
                    min_ele = step

                    for i in range(min_ele + 1,size):
                        if self.array[i] < self.array[min_ele]:
                            min_ele = i

                    (self.array[step],self.array[min_ele]) = (self.array[min_ele],self.array[step])
                
                return self.array
            else :
                logger.warning("List is Empty")
        except Exception as e:
            logger.error(f"Error : {str(e)}")

    def display_sorted_array(self,sorted_array):
        print(f"The sorted array is: {sorted_array} ")


# Bubble sort
class BubbleSorting(Sorting):

    def __init__(self,array_of_numbers) -> None:
        self.array=array_of_numbers


    def sorting_algo(self):
        try:
            """
            Description : 
                    This function sorts number from the list using bubble sort algo.
            Parameters :
                    self : To get list of user input numbers declared in constructor.
            Returns    :
                    array : sorted list of numbers.
            """
            size = len(self.array)

            if size > 0:

                temp = 0
                for i in range(size-1):
                    for j in range(size - i -1):
                        if self.array[j] > self.array[j+1]:
                            self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]                
                    
                return self.array
            else :
                logger.warning("List is Empty")
        except Exception as e:
            logger.error(f"Error : {str(e)}")


    def display_sorted_array(self,sorted_array):
        print(f"The sorted array is: {sorted_array} ")


# merge sort
class MergeSorting(Sorting):
    def __init__(self, array_of_numbers):
        self.array = array_of_numbers

    def sorting_algo(self):
        """
            Description : 
                    This function sorts number from the list using merge sort algo.
            Parameters :
                    self : To get list of user input numbers declared in constructor.
            Returns    :
                    array : sorted list of numbers.
        """
        try:
            if len(self.array) > 1:
                mid = len(self.array) // 2
                lefthalf = self.array[:mid]
                righthalf = self.array[mid:]

                lefthalf_sort = MergeSorting(lefthalf)
                righthalf_sort = MergeSorting(righthalf)

                lefthalf_sorted = lefthalf_sort.sorting_algo()
                righthalf_sorted = righthalf_sort.sorting_algo()

                sorted_array = []
                i = j = 0

                while i < len(lefthalf_sorted) and j < len(righthalf_sorted):
                    if lefthalf_sorted[i] < righthalf_sorted[j]:
                        sorted_array.append(lefthalf_sorted[i])
                        i += 1
                    else:
                        sorted_array.append(righthalf_sorted[j])
                        j += 1

                while i < len(lefthalf_sorted):
                    sorted_array.append(lefthalf_sorted[i])
                    i += 1

                while j < len(righthalf_sorted):
                    sorted_array.append(righthalf_sorted[j])
                    j += 1

                self.array = sorted_array
            return self.array
        
        except Exception as e:
            return []

    def display_sorted_array(self,sorted_array):
        print(f"The sorted array is: {sorted_array}")

