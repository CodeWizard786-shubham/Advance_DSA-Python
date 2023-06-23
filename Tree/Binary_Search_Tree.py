'''
@Author: Shubham shirke
@Date: 2023-06-22 17:10:30
@Last Modified by: Shubham shirke
@Last Modified time: 2023-06-22 17:29:30
@Title : Implement a binary search tree and write functions to insert, delete, and search for a node.
'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:

    def inorder(self, root):
        """
        Description : 
                This function shows the traversal in the tree.
        Parameters :
                self :default constructor.
                root : root node of the tree.
        """
        if root is not None:
            self.inorder(root.left)
            print(str(root.key) + "->", end=' ')
            self.inorder(root.right)

    def insert(self, node, key):
        """
        Description : 
                    This function insert input integers into the tree nodes.
        Parameters  :
                    node : node to insert element
                    key  : value to insert
        returns     : 
                    node : node with value.
        """
        if node is None:
            return Node(key)
        
        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        return node
    

    def min_value_node(self, node):
        """
        Description : 
                This function finds minimum value node to switch nodes for deletion.
        Parameters  :
                self : default constructor 
                node : nodes of the tree.
        Returns     :
                current : min value node
        """
        current = node

        while current.left is not None:
            current = current.left

        return current
    

    def delete_node(self, root, key):
        """
        Description : 
                This function searches the node to delete finds the child nodes and accordingly switch node places and then delete the required node. 
        Parameters  :
                root : root node
                key  : value to delete 
        """
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)

            root.key = temp.key

            root.right = self.delete_node(root.right, temp.key)

        return root
    
    def search_node(self, root, key):
        """
        Description : 
                    This function searches the key to see if it is present in the tree.
        Parameters  :
                    root : root of the tree
                    key : value to search
        """
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search_node(root.left, key)
        else:
            return self.search_node(root.right, key)


# main
def main():
    binarysearch = BinarySearchTree()
    root = None
    root = binarysearch.insert(root, 8)
    root = binarysearch.insert(root, 3)
    root = binarysearch.insert(root, 1)
    root = binarysearch.insert(root, 6)
    root = binarysearch.insert(root, 7)
    root = binarysearch.insert(root, 10)
    root = binarysearch.insert(root, 14)
    root = binarysearch.insert(root, 4)

    print("--Binary Search Tree Algorithm--")
    print("Inorder traversal: ", end=' ')
    binarysearch.inorder(root)

    print("\nDelete 10")
    root = binarysearch.delete_node(root, 10)

    print("Inorder traversal: ", end=' ')
    binarysearch.inorder(root)

    key = 14
    result = binarysearch.search_node(root, key)
    if result:
        print(f"\n Number Found")
    else:
        print(f"\n{result} not found")



if __name__ == "__main__":
    main()
