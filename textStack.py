"""
This is a stack created by a linked list. This will be used for
the text editor logic.
"""
class Stack:
    """Class used with a first in first out basis. Uses a linked list as the data structure"""

    def __init__(self, initStack=[]):
        """Initializer for the stack class. Defualts with an empty linked list"""
        self.head = None
        if not isinstance(initStack, list):
            raise ValueError("When initializing the stack, you must use a list object")
        if initStack: #If there are items in the stack
            for i in initStack[::-1]:
                self.append(i)

    class __Node:
        """A private node class used as the data points in the linked list"""
        def __init__(self, data, next = None):
            """Initializer for the Node"""
            self.data = data
            self.next = next

    def append(self, item):
        """Adds an item to the stack"""
        self.head = self.__Node(item, self.head)

    def pop(self):
        """Removes the top element in the stack and returns the value"""
        if self.head is None:
            raise IndexError("You can't use pop() with no elements in the stack")
        tmp = self.head
        self.head = self.head.next
        return tmp.data

    def peek(self):
        """Returns, but doesn't remove, the top element from the stack"""
        if self.head is None:
            raise IndexError("You can't use peek() with no elements in the stack")
        tmp = self.head.data
        return tmp
    
    def __str__(self):
        """Returns the stack as a string object"""
        output = "["
        if self.head is None:
            return output + "]"
        cursor = self.head
        while cursor.next is not None:
            if isinstance(cursor.data, str):
                output +=  "'" + str(cursor.data) + "', "
            else:
                output += str(cursor.data) + ", "
            cursor = cursor.next
        if cursor.next is None:
            if isinstance(cursor.data, str):
                output +=  "'" + str(cursor.data) + "'"
            else:
                output += str(cursor.data)
        return output + "]"
    
    def __repr__(self):
        """Returns the stack as a string"""
        output = "["
        if self.head is None:
            return output + "]"
        cursor = self.head
        while cursor.next is not None:
            if isinstance(cursor.data, str):
                output +=  "'" + str(cursor.data) + "', "
            else:
                output += str(cursor.data) + ", "
            cursor = cursor.next
        if cursor.next is None:
            if isinstance(cursor.data, str):
                output +=  "'" + str(cursor.data) + "'"
            else:
                output += str(cursor.data)
        return output + "]"

    def __len__(self):
        """Returns the length of the stack"""
        cursor = self.head
        length = 0
        while cursor is not None:
            length += 1
            cursor = cursor.next
        return length
