# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r_list = []

        def insertNode(val):
            r_list.append(val)

        while (l1 != None) or (l2 != None):
            if l1 == None:
                insertNode(l2.val)
                l2 = l2.next
            elif l2 == None:
                insertNode(l1.val)
                l1 = l1.next
            else:
                if l1.val < l2.val:
                    insertNode(l1.val)
                    l1 = l1.next
                else:
                    insertNode(l2.val)
                    l2 = l2.next
                    
        return r_list            

if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(5)

    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(6)

    print(solution.mergeTwoLists(l1,l2))