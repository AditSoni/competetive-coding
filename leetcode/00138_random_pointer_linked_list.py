
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# learn this solution
class Solution:

    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        if head in self.visited:
            return self.visited[head]
        
        node = Node(head.val, None, None)

        self.visited[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node
    

# my solution

index_map = {}
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        head2 = Node(x=head.val) if head else None
        new = head2
        old = head
        index = 0
        while head and head.next:
            index_map[hex(id(head))] = index
            head2.next = Node(x=head.next.val)
            head = head.next
            head2 = head2.next
            index += 1
        index_map[hex(id(head))] = index
        # start with old 
        # find random if exists
        head1 = new
        while old :
            if old.random is not None:
                node1 = findNode(head1,index_map[hex(id(old.random))])
                new.random = node1
            old = old.next
            new = new.next
        
        return head1
    
def findNode(head,index_):
    index_new = 0
    while head :
        if index_new == index_:
            return head
        head = head.next
        index_new+=1
    return None
    

