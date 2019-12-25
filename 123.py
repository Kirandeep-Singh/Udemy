# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        str1 = "".join([str(i) for i in l1[::-1]])
        str2 = "".join([str(i) for i in l2[::-1]])
        revsum = str(int(str1) + int(str2))[::-1]

        #revsum = str(int("".join([str(i) for i in l1[::-1]]))+ int("".join([str(i) for i in l2[::-1]])))[::-1]
        # return [i for i in revsum]

l1 = [2,4,3]
l2 = [5,6,4]

#print (Solution.addTwoNumbers(Solution,l1,l2))

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing


node1 = Node(12)
node2 = Node(99)
node3 = Node(13)

node1.next = node2
node2.next = node3

'''

import mony

mony.abc()





