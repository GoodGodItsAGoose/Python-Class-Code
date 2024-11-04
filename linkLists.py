# class Node:
#     def __init__(self, data):
#         # initialize the node
#         self.data = data
#         # set the pointer to none
#         self.next = None #null, no value associated with variable

# class Linked_List:
#     def __init__(self):
#         # set the head to the linked list to None
#         self.head = None
    
#     # append method O(n)
#     def append(self, data):
#         node = Node(data)
#         if self.head is None:
#             # sets the data to the head node
#             self.head = node
#             return
#         else:
#             last = self.head
#             while(last.next):
#                 last = last.next
#             last.next = node
            
#     def printList(self):
#         temp = self.head
#         while(temp):
#             print(temp.data)
#             temp = temp.next

# LL = Linked_List()

# LL.append(8)

# LL.append(81)

# LL.append(817)

# LL.printList()



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Linked_list:
#     def __init__(self):
#         self.head = None
    
#     def insertAtBeginning(self, data):
#         # Create a new node from the data
#         node = Node(data)
        
#         node.next = self.head
#         
#         # Update the head to be the new node
#         self.head = node
    
#     def display(self):
#         # Set the head node we want to loop through
#         current = self.head
        
#         # Loop through the nodes in the linked list
#         while current:
#             print(current.data, end = " -> ")
#             current = current.next
#         print("None")
        
# LL = Linked_list()
# LL.insertAtBeginning(10)
# LL.insertAtBeginning(20)
# LL.insertAtBeginning(30)
# LL.display()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linked_List:
    def __init__(self):
        self.head = None
        
    def insertAtBeginning(self,data):
        # Create a whole new node! Woah!
        node = Node(data)
        
        # Pass the head to the next node
        node.next = self.head
        
        # Update the head to the new node
        self.head = node
    
    def displayResults(self):
        # Set the head node to loop through
        current = self.head
        
        # Loop through the said head node
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print("None")
        
books = Linked_List()

# Existing books
books.insertAtBeginning("To Kill a Mockingbird")
books.insertAtBeginning("1984")
books.insertAtBeginning("The Great Gatsby")

# Adding books
books.insertAtBeginning("Moby Dick")
books.insertAtBeginning("War and Peace")
books.insertAtBeginning("Pride and Prejudice")

# Printing book names
books.displayResults()

# To answer your question,
# Why don't you run the code and find out?
