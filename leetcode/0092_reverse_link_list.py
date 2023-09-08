#### optimal solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        pre = dummy
        cur = dummy.next
        
        # find the position
        for i in range(1,left):
            cur = cur.next
            pre = pre.next
        
        
        # reverse
        for i in range(right-left):
            temp = cur.next
            cur.next = temp.next
            temp.next  = pre.next
            pre.next = temp
        
        return dummy.next
    
### my solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        index = 1
        if left == right:
            return head
        list_head = head
        left_node = detached_left_node = None
        previous = None
        while head:
            print(head.val)
            if index < left:
                index+=1
                previous = head
                head=head.next
            if index == left:
                print('index == left')

                if index == 1:
                    list_head=None
                left_node = previous
                next_node = head.next
                detached_left_node = head
                detached_left_node.next = None
                previous = detached_left_node
                head = next_node
                index+=1
            elif index == right:
                print('index == right')
                next_node = head.next
                head.next = previous
                previous = head

                if left_node is not None:
                    left_node.next = head
                    if next_node is not None:
                        detached_left_node.next = next_node
                    return list_head
                if next_node == None:
                    return head
                detached_left_node.next = next_node
                if list_head == None:
                    list_head = previous
                    return list_head
            
                index+=1
            elif index > left:
                print('index > left')
                next_node = head.next
                head.next = previous
                previous = head
                head = next_node
                index+=1
            
        
        return list_head


