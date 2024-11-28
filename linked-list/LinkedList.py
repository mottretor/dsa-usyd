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
            
