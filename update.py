class Node :
    def __init__ ( self, data ) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__ ( self ) :
        self.head = None
        
    def printList ( self ) :
        temp = self.head
        while ( temp ) :
            print ( temp.data )
            temp = temp.next
            
    def update ( self , replace, replace_with ) :
        find = self.head
        while ( find.data != replace ) :
            find = find.next
        find.data = replace_with

llist = LinkedList()
llist.head = Node ( 1 )
llist.head.next = Node ( 2 )
llist.head.next.next = Node ( 3 )
llist.update ( 2 , 5 )
llist.printList()