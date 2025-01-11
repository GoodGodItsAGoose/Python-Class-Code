class Node:
    # [node | next]
    def __init__(self, data):
        self.data = data
        # [node = data]
        self.next = None
        # [next = none]
        
# [Head pointer ->  current head  ->      tail      -> none]
# [    head     ->   [(10)-->]    ->   [(20)-->]    -> none]
# [ (data) | (pointer) (data) | (pointer)]

class linked_list:
    def __init__(self):
        self.head = None
        # [Head -> None] (initializes an empty list)
    
    def insert_at_beginning(self, data):
        node = Node(data)
        # creates [Head--> [(new data)-->] None]
        
        node.next = self.head
        # [[(new data)-->] to [(new data)--> [Head-->] ] ]
        
        self.head = node
        # Old: [Head--> [(anything else)--> [None] ] ] 
        # Inserting: [(new data)--> [Head--> [(anything else)--> [None] ] ] ]
        # New: [Head--> [(new data)--> [(anything else)--> [None] ] ] ]
        
    def find_node(self, node_data):
        cur_node = self.head
        num = 0
        while cur_node:
            if cur_node.data == node_data:
                return num
            else:
                cur_node = cur_node.next
                num += 1
                
    def edit_node(self, num):
        finder = input("Input node data to edit: ")
        self.find_node(int(finder))
        # make a change node function
    
    def insert_at_end(self, data):
        node = Node(data)
        #Checks if empty
        #If it is, sets head to beginning of list
        if self.head is None:
            node.next = self.head
            self.head = node
        #If the list is not empty, goes through each node until the end. Then adds new node.
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            node.next = self.head
            self.head = node
    
    def display(self):
        temp = self.head
        # [Temp(Head)-->[(Data)-->[None]]
        while temp:
            print(temp.data, end=" ")
            
            temp = temp.next
            # [(Head)-->[Temp(data)-->[None]]]
ll = linked_list()
ll.insert_at_beginning(15)
ll.insert_at_beginning(25)
ll.insert_at_beginning(35)
ll.insert_at_beginning(45)
ll.insert_at_beginning(55)
print(ll.find_node(35))
ll.display()        
