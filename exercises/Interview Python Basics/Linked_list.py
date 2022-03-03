class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


def reverse_linked_list(llist: LinkedList):
    prev = None
    curr = llist.head
    i = 0
    while(curr):
        next = curr.next
        curr.next = prev
        if (next == None):
            llist.head = curr
        prev = curr
        curr = next
        i += 1


def detect_loop(llist: LinkedList):
    s = set()
    temp = llist.head
    while(temp):
        if temp.data in s:
            return True
        else:
            s.add(temp.data)
        temp = temp.next
    return False


def n_node_end(llist: LinkedList, n):
    res = []
    temp = llist.head
    while(temp):
        if len(res) < n:
            res.append(temp.data)
        else:
            res.pop(0)
            res.append(temp.data)
        temp = temp.next
    return res


def remove_duplicates(llist: LinkedList):
    s = set()
    temp = llist.head
    ant = None
    while(temp):
        if temp.data in s:
            ant.next = temp.next.next if temp.next else None
            print("remove")
        else:
            s.add(temp.data)
        ant = temp
        temp = temp.next


def main():
    # Driver code
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)

    print("Given Linked List")
    llist.printList()

    # reverse_linked_list(llist)
    # print("\nReversed Linked List")
    # llist.printList()
    # print("\n")

    # llist.head.next.next.next.next = llist.head
    # print("Loop", detect_loop(llist))

    # print(n_node_end(llist, 2))

    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(20)
    llist.push(85)

    print("Given Linked List")
    llist.printList()
    remove_duplicates(llist)
    print("\nRemove duplicates")
    llist.printList()


if __name__ == "__main__":
    main()
