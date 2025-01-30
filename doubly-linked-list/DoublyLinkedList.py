from DoublyLinkedListNode import DoublyLinkedListNode

class DoublyLinkedList:

    def __init__(self):
        self.head = None
    
    def add(self, data):
        new_node = DoublyLinkedListNode()
        new_node.data = data
        
        if(self.head == None):
            self.head = new_node
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = new_node
            new_node.prev = current
    
    def insert(self, data, index):
        new_Node = DoublyLinkedListNode()
        new_Node.data = data
        if(index == 0):
            if(self.head == None):
                self.head = new_Node
            else:
                new_Node.next = self.head
                self.head.prev = new_Node
                self.head = new_Node
        else:
            if(self.head == None):
                print("Error!!! Index out of bounds")
            else:
                current = self.head
                count = 0
                while(current != None and count+1 < index):
                    current = current.next
                    count += 1
                if(current == None):
                    print("Error!!! Index out of bounds")
                else:
                    if(current.next != None):
                        new_Node.next = current.next
                        current.next.prev = new_Node
                    current.next = new_Node
                    new_Node.prev = current

    def remove(self, index):
        if(self.head == None):
            print("Error!!! Index out of bounds")
        elif(index == 0):
            temp = self.head
            self.head = temp.next
            temp.next = None
            if(self.head != None):
                self.head.prev = None
        else:
            current = self.head
            count = 0
            while(current!=None and count < index):
                current = current.next
                count += 1            
            if(current == None):
                print("Error!!! Index out of bounds")
            else:
                temp = current
                current = temp.prev
                current.next = temp.next
                temp.next = None
                temp.prev = None
                if(current.next != None):
                    current.next.prev = current

    def set(self, data, index):
        if(self.head == None):
            print("Error!!! Index out of bounds")
        else:
            current = self.head
            count = 0

            while(current != None and count < index):
                current  = current.next
                count += 1
            
            if(current == None):
                print("Error!!! Index out of bounds")
            else:
                current.data = data

    def get(self, index):
        if(self.head == None):
            print("Error!!! Index out of bounds")
        else:
            current = self.head
            count = 0

            while(current != None and count < index):
                current  = current.next
                count += 1
            
            if(current == None):
                print("Error!!! Index out of bounds")
            else:
                return current.data

    def __str__(self):
        temp_str = "["
        if(self.head == None):
            temp_str += "]"
            return temp_str
        else:
            current = self.head
            while(current != None):
                temp_str += str(current.data)
                current = current.next
                if(current!=None):
                    temp_str += ", "
            temp_str += "]"
            return temp_str