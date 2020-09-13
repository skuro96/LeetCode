# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ans = ListNode()
        inc = False
        
        while 1:
            ans.val = l1.val + l2.val
            if inc == True:
                ans.val += 1
                inc = False
            if ans.val >= 10:
                ans.val %= 10
                inc = True
            if (l1.next != None and l2.next != None):
                l1 = l1.next
                l2 = l2.next
                ans.next = ListNode()
                ans = ans.next
            else:
                break
        
        if l1.next != None:
            l1 = l1.next
            ans.next = ListNode()
            ans = ans.next
            while 1:
                ans.val = l1.val
                if inc == True:
                    ans.val += 1
                    inc = False
                if ans.val >= 10:
                    ans.val %= 10
                    inc = True
                if l1.next != None:
                    l1 = l1.next
                    ans.next = ListNode()
                    ans = ans.next
                else:
                    break
                    
        elif l2.next != None:
            l2 = l2.next
            ans.next = ListNode()
            ans = ans.next
            while 1:
                ans.val = l2.val
                if inc == True:
                    ans.val += 1
                    inc = False
                if ans.val >= 10:
                    ans.val %= 10
                    inc = True
                if l2.next != None:
                    l2 = l2.next
                    ans.next = ListNode()
                    ans = ans.next
                else:
                    break
                    
        if inc == True:
            ans.next = ListNode()
            ans = ans.next
            ans.val += 1
            
        return ret