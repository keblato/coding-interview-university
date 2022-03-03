import copy
from queue import Queue


def reverse_first_k_elem(q: Queue, k: int):
    stack = []
    # Saco los elementos hasta k
    for i in range(k):
        stack.append(q.get())

    # Los meto al final
    while (len(stack) != 0):
        q.put(stack[-1])
        stack.pop()
    # Saco los elementos restantes para volverlos a meter
    for _ in range(Queue.qsize(q) - k):
        temp = q.get()
        q.put(temp)


def printQueue(q: Queue):
    while (not q.empty()):
        print(q.queue[0], end=" ")
        q.get()


def main():
    q = Queue()
    q.put(10)
    q.put(20)
    q.put(30)
    q.put(40)
    q.put(50)
    q.put(60)
    q.put(70)
    q.put(80)
    q.put(90)
    q.put(100)
    q2 = Queue()
    for i in q.queue:
        q2.put(i)
    # printQueue(q2)
    # print("\n")
    # reverse_first_k_elem(q, 4)
    # printQueue(q)
    # print("\n")


if __name__ == "__main__":
    main()
