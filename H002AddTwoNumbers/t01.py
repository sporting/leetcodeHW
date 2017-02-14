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
            if (l1 is None) and (l2 is None):
                if carry > 0:
                    cur.next = ListNode(carry)
                break
            v1 = 0 if l1 is None else (l1.val if l1.val is not None else 0)
            v2 = 0 if l2 is None else (l2.val if l2.val is not None else 0)

            total = v1 + v2 + carry
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

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

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
    l2 = createListNode([5,6])

    solution = Solution()
    answer = solution.addTwoNumbers(l1,l2)
    print listNodeToArray(answer)
