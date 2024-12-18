from LinkedListNode import LinkedListNode

class LinkedList:

    def __init__(self):
        self.head = None
    
    def add(self, data):
        new_node = LinkedListNode()
        new_node.data = data
        
        if(self.head == None):
            self.head = new_node
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = new_node
    
    def insert(self, data, index):
        new_Node = LinkedListNode()
        new_Node.data = data
        if(index == 0):
            if(self.head == None):
                self.head = new_Node
            else:
                new_Node.next = self.head
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
                    new_Node.next = current.next
                    current.next = new_Node
                

    def remove(self, index):
        if(self.head == None):
            print("Error!!! Index out of bounds")
        elif(index == 0):
            temp = self.head
            self.head = temp.next
            temp.next = None
        else:
            current = self.head
            count = 0
            while(current.next!=None and count+1 < index):
                current = current.next
                count += 1            
            if(current.next == None):
                print("Error!!! Index out of bounds")
            else:
                temp = current.next
                current.next = temp.next
                temp.next = None


            
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
            
