# Definition for singly-linked list.
from decimal import Inexact
from sre_constants import IN


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    act = head
    i = 0
    dad = None
    target = head
    dist = 1
    while(act != None):
        # print("dist", dist)
        if dist > n:
            print("entre")
            dad = target
            target = target.next
            dist = n
            # print("resProc", res.val)

        act = act.next
        # print("-----------", act.val if act != None else "")
        dist += 1
    if dad != None:
        targetNext = target.next
        dad.next = targetNext
    else:
        return head.next

    return head


def main():
    toList = [1, 2]
    head = ListNode()
    next = head
    for i, a in enumerate(toList):
        next.val = a

        next.next = ListNode()
        if i == len(toList)-1:
            next.next = None
        next = next.next

    print(removeNthFromEnd(head, 2))


if __name__ == "__main__":
    main()
