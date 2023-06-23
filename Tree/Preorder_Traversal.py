'''
@Author: Shubham shirke
@Date: 2023-06-22 22:20:30
@Last Modified by: Shubham shirke
@Last Modified time: 2023-06-22 22:20:30
@Title : Write a program to perform a pre-order traversal of a binary tree recursively.
'''

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


def Preorder(root):
    """
    Description : 
            This function traverses the tree in preorder.
    Parameters :
            root : root node
    returns :
            none 
    """
    if root:
        # First print the data of node
        print(root.val, end=" "),

        # Then recur on left child
        Preorder(root.left)

        # Finally recur on right child
        Preorder(root.right)


# main
def main():
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	print("Preorder traversal of binary tree is")
	Preorder(root)


if __name__ == "__main__":
	main()