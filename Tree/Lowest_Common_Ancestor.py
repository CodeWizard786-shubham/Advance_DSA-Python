'''
@Author: Shubham shirke
@Date: 2023-06-22 19:20:30
@Last Modified by: Shubham shirke
@Last Modified time: 2023-06-22 19:20:30
@Title : Given a binary tree, write a program to find the lowest common ancestor of two nodes.
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

    def find_lca(self,root, key1, key2):
        """
        Description : 
                This function finds the lowest common ancestor between 
        Parameters :
                root : root of the tree
                key1 : value 1
                key2 : value 2
        Returns     :
                root : lowest common ancestor between key 1 and key 2.
        """
        if root is None:
            return None

        # If both keys are less than the root key, LCA must be in the left subtree
        if key1 < root.key and key2 < root.key:
            return self.find_lca(root.left, key1, key2)

        # If both keys are greater than the root key, LCA must be in the right subtree
        if key1 > root.key and key2 > root.key:
            return self.find_lca(root.right, key1, key2)

        # If one key is less than or equal to the root key and the other key is greater than or equal to the root key,
        # then the root is the LCA
        return root

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

    key1 = 4
    key2 = 7

    print("--Lowest Common Ancestor--")
    print("Inorder traversal: ", end=' ')
    binarysearch.inorder(root)

    lca = binarysearch.find_lca(root, key1, key2)

    if lca:
        print("Lowest Common Ancestor of", key1, "and", key2, "is:", lca.key)
    else:
        print("Lowest Common Ancestor not found")


if __name__ == "__main__":
    main()
