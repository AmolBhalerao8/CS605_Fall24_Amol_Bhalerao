Binary Search Tree (BST)
This is a simple implementation of a Binary Search Tree (BST) where each node stores:

A name (key)
A phone number (value)
You can use this tree to insert new names with their associated phone numbers, search for a phone number by name, delete a name from the tree, and display the entire directory in alphabetical order using an in-order traversal.

Features
Insert a new contact:

Add a new name and phone number to the tree.
The tree automatically places the name in the correct position to maintain the binary search tree property.

Search for a contact:
Look up a phone number by providing a name. If the name exists in the tree, it returns the phone number; otherwise, it informs you that the name was not found.

In-order traversal:
Display all the names in the phone directory in alphabetical order, along with their associated phone numbers.

Delete a contact (optional extra credit):
Remove a name and phone number from the tree. The tree handles cases where the contact has no children, one child, or two children.

Files
main.py: Contains the implementation of the TreeNode and BinarySearchTree classes with methods for inserting, searching, deleting, and in-order traversal.

Requirements
Python 3.x

How to Run
Clone the repository or copy the main.py file or download the .ipynb/.py file and run in any python environment.
Run the main.py file in your Python environment.
Use the methods provided to insert, search, delete, or traverse the binary search tree.
