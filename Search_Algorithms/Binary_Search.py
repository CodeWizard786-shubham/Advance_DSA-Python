'''
@Author: Shubham shirke
@Date: 2023-06-21 14:30:30
@Last Modified by: Shubham shirke
@Last Modified time: 2023-06-21 14:30:30
@Title : Implement the binary search algorithm to search for a target element in a sorted array.
'''

class BinarySearch:

    def __init__(self, list_of_numbers):
        # default constructor
        self.binary_list = list_of_numbers


    def binarysearch(self, l, r, number_search):
        """
        Description : 
                This function uses recursive divide and conquer strategy to seach  the given element from the list.
        Parameters  :
                self : default constructor containing list of elements.
                l : represent left index of the list.
                r : represent right index of the list.
                number_search : number to check in list if present.
        Returns :
                -1   : indicating number not found in list
        
        """
        if r >= l:
            mid = l + (r - l) // 2

            if self.binary_list[mid] == number_search:
                return mid

            elif self.binary_list[mid] > number_search:
                return self.binarysearch(l, mid - 1, number_search)

            else:
                return self.binarysearch(mid + 1, r, number_search)

        return -1

# main
def main():
    number_list = list(input("Enter numbers to insert in list (separated by commas): ").split(","))
    list_of_numbers = [int(num) for num in number_list]
    number_search = int(input("Enter number to search: "))
    binary = BinarySearch(list_of_numbers)
    index_number = binary.binarysearch(0, len(list_of_numbers) - 1, number_search)
    
    if index_number != -1:
        print(f"Number found at position: {index_number + 1}")
    else:
        print("Number not found in the list")


if __name__ == "__main__":
    main()
