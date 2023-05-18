#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)

# Complete the mergeLists function below.


# For your reference:

# class SinglyLinkedList:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.next = None

def mergeLists(head1, head2):
    if head1 and head2:
        if head1.data < head2.data:
            master_node = SinglyLinkedListNode(head1.data)
            head1 = head1.next
        else:
            master_node = SinglyLinkedListNode(head2.data)
            head2 = head2.next

        pointer = master_node

        while head1 or head2:
            if head1 and head2:
                if head1.data  <= head2.data:
                    pointer.next = SinglyLinkedListNode(head1.data)
                    head1 = head1.next
                else:
                    pointer.next = SinglyLinkedListNode(head2.data)
                    head2 = head2.next
            elif head1:
                pointer.next = SinglyLinkedListNode(head1.data)
                head1 = head1.next
            else:
                pointer.next = SinglyLinkedListNode(head2.data)
                head2 = head2.next

            pointer = pointer.next

        return master_node
    elif head1:
        return head1
    else:
        return head2

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ')
        # fptr.write('\n')

    # fptr.close()
