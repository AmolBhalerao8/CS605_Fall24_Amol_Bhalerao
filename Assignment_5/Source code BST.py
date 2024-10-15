#!/usr/bin/env python
# coding: utf-8

# In[9]:


class TreeNode:
    def __init__(self, name, phone_number):
        self.name = name 
        self.phone_number = phone_number  
        self.left = None
        self.right = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Operation for inserting a new node
    def insert(self, name, phone_number):
        new_node = TreeNode(name, phone_number)
        if self.root is None:
            self.root = new_node  # Here first node will become the root
        else:
            current = self.root
            while True: 
                if name < current.name:  # it will go to the left subtree
                    if current.left is None:
                        current.left = new_node 
                        break
                    else:
                        current = current.left
                elif name > current.name:  # it will go to the right subtree
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    # Operation for searching for a phone number by name
    def search(self, name):
        current = self.root
        while current is not None:
            if name == current.name:
                return current.phone_number  
            elif name < current.name:
                current = current.left
            else:
                current = current.right 
        return None

    # Operation for In-order traversal
    def inorder_traversal(self):
        stack = []
        current = self.root

        while current is not None or stack:
            while current is not None:
                stack.append(current)  # here we are pushing left nodes onto the stac
                current = current.left

            current = stack.pop() 
            print(f"{current.name}: {current.phone_number}")

            current = current.right

   
    def delete(self, name):
        self.root = self.deleterec(self.root, name)

    # deletion operation
    def deleterec(self, node, name):
        if node is None:
            return node

        if name < node.name:
            node.left = self.deleterec(node.left, name)
        elif name > node.name:
            node.right = self.deleterec(node.right, name)
        else:
        
            # if there is no child (leaf node)
            if node.left is None and node.right is None:
                return None

            # if there is one child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # if there are two children
            smallest = self.find_min(node.right)
            node.name = smallest.name
            node.phone_number = smallest.phone_number
            node.right = self.deleterec(node.right, smallest.name)

        return node

    # method to find the minimum value node in a subtree
    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

# Example:
if __name__ == "__main__":
    bst1 = BinarySearchTree()
    bst1.insert("AAAA", "555-1234")
    bst1.insert("BBBB", "555-2345")
    bst1.insert("CCCC", "555-3456")
    bst1.insert("DDDD", "555-5555")
    bst1.insert("EEEE", "555-5553")
    bst1.insert("CDSF", "555-5534")
    bst1.insert("ABCD", "555-5532")
    bst1.insert("ASED", "555-5643")
    bst1.insert("CSAD", "555-557")
    bst1.insert("ZZZZ", "555-555755")
    


    # Searching phone numbers
    print(bst1.search("AAAA")) 
    print(bst1.search("D"))    
    print(bst1.search("BBBB"))

    # In-order traversal
    bst1.inorder_traversal()

    # Deleting a node
    bst1.delete("CCCC")
    bst1.delete("DDDD")
    bst1.inorder_traversal()


# In[ ]:




