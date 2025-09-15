


class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    # Them vao cuoi danh sach
    def insert_last(self, key):
        if self.head is None:
            self.head = Node(key)
        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = Node(key)
            
    # Them vao dau danh sach
    def insert_first(self, key):
        if self.head is None:
            self.head = Node(key)
        else:
            new_node_first = Node(key)
            new_node_first.next = self.head
            self.head = new_node_first
    
    # Xoa phan tu o cuoi danh sach
    def remove_last(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
        else:
            tmp = self.head
            while tmp.next.next is not None:
                tmp = tmp.next
            tmp.next = None
            
    def show(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.key, end=' ')
            tmp = tmp.next
        print()
            
            
if __name__ == "__main__":
    ll = LinkedList()
    
    for i in range(6, 11, 1):
        ll.insert_last(i)
    for i in range(5, 0, -1):
        ll.insert_first(i)
        
    ll.show()
    
    for i in range(5):
        ll.remove_last()
    
    ll.show()
    
    
    
            