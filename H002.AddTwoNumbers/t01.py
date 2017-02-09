# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        s1, cur = None, None

        while True:
            if l1 is None:
                break
            total = l1.val + l2.val + carry
            if total > 9:
                total = total - 10
                carry =1
            else:
                carry =0
            if s1 is None:
                s1 = ListNode(total)
                cur = s1
            else:
                cur.next = ListNode(total)
                cur = cur.next

            l1 = l1.next
            l2 = l2.next

        return s1

def createListNode(llist):
    ll, cur = None, None
    for l1 in llist:
        if ll is None:
            ll = ListNode(l1)
            cur = ll
        else:
            cur.next = ListNode(l1)
            cur = cur.next

    return ll

def listNodeToArray(listnode):
    result = []
    while True:
        if listnode is None:
            break
        result.append(listnode.val)
        listnode = listnode.next

    return result 

if __name__ == "__main__":
    l1 = createListNode([2,4,3])
    l2 = createListNode([5,6,4])

    solution = Solution()
    answer = solution.addTwoNumbers(l1,l2)
    print listNodeToArray(answer)
