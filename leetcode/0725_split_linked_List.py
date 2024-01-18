# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.node_list = []

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        # size of list 
        # size =  k return same
        # separate each element
        #
        # size > k  find mod

        # size < k  add empty nodes

        # find  size
        # my solution
        list_head1 = head
        size = 0
        if k == 1:
            return [head]

        while head:
            size+=1
            self.node_list.append(ListNode(val=head.val))
            head = head.next
        
        if size == k:
            return self.node_list
        elif size < k :
            print('separate each node and add null nodes')
            number_of_new_nodes = k - size
            return self.node_list + [ListNode(val='')]*number_of_new_nodes
        else: # size > k
            output_array = []
            length_of_normal,extra_nodes = divmod(size , k)
            i = 0
            while i < size:
                print("Node value",self.node_list[i].val)
                temp = None
                j = 0
                flag = True
                current_length = length_of_normal
                if extra_nodes !=0:
                    extra_nodes -=1
                    current_length = length_of_normal + 1
                while j < current_length:
                    print("j ",j)
                    if flag:
                        list_head = self.node_list[i]
                        temp = list_head
                        flag = False
                    
                    if i >= size-1:
                        break
                    print(f" i in j = {i}")
                    print(temp.val,temp.next.val if temp.next else None)
                    print("head ",list_head)

                    if j < (current_length - 1):
                        temp.next = self.node_list[i+1]
                        temp = temp.next
                        i+=1
                        print("i in inner j",i)
                    
                    
                    j+=1
                
                temp = None
                print("Appendinggg ",list_head)
                output_array.append(list_head)
                i+=1
                
            print(output_array)
            return output_array

        # optimized solution
def ans(head,ListNode,k):
        
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        # print(count)

        part_size  = count // k
        extra = count % k

        output = [None] * k
        prev = ListNode(0)
        prev.next = cur = head
        i = 0

        while cur:
            part = part_size
            if extra:
                part += 1
                extra -= 1
            
            output[i] = cur

            while part:
                prev, cur = cur, cur.next
                part -= 1
            prev.next = None
            i += 1
        
        # print(output)
        return output
        