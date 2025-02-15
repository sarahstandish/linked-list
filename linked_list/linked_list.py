
# Defines a node in the singly linked list
from re import sub


class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None # keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        if (self.head != None):
            return self.head.value

        return None

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        self.head = Node(value, self.head)

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        if (self.head == None):
            return False

        curr = self.head
        while (curr != None):
            if curr.value == value:
                return True
            curr = curr.next

        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        count = 0
        curr = self.head
        while (curr != None):
            count += 1
            curr = curr.next

        return count

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        i = 0
        curr = self.head
        while (curr != None):
            if i == index:
                return curr.value
            curr = curr.next
            i += 1
        return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        
        if (self.head == None):
            return None
        curr = self.head
        while (curr.next != None):
            curr = curr.next
        return curr.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        if (self.head == None):
            self.add_first(value)
        else:
            curr = self.head
            while (curr.next != None):
                curr = curr.next
            curr.next = Node(value)

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        if self.head == None:
            return None
        
        curr = self.head
        max = curr.value
        while (curr != None):
            if curr.value > max:
                max = curr.value
            curr = curr.next

        return max

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        if self.head == None:
            return None
        
        if self.head.value == value:
            self.head = self.head.next
        else:
            curr = self.head
            while (curr.next.value != value):
                curr = curr.next
            curr.next = curr.next.next

        

    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self):
        if self.head == None:
            return None
        if self.head.next == None:
            return self.head

        subsequent = self.head.next
        self.head.next = None
        curr = self.head
        while (subsequent != None):
            temp = subsequent.next
            subsequent.next = curr
            curr = subsequent
            subsequent = temp
        self.head = curr
            

    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        if self.head == None:
            return None
        if self.head.next == None:
            return self.head
        count = 0
        middle = self.head
        current = self.head
        while current:
            current = current.next
            count += 1
            if count % 2 == 0:
                middle = middle.next

        return middle.value

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        if self.head == None:
            return None
        curr = self.head
        nth = None
        count = 0

        while curr:
            if count == n:
                nth = self.head
            elif count > n:
                nth = nth.next
            curr = curr.next
            count += 1

        if nth == None:
            return nth
        return nth.value

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def has_cycle(self):
        pass        

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head # make the last node link to first node
