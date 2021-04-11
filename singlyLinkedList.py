class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key)


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def printList(self):  # 변경없이 사용할 것!
        v = self.head
        while(v):
            print(v.key, "->", end=" ")
            v = v.next
        print("None")

    def pushFront(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pushBack(self, key):
        new_node = Node(key)
        if self.size == 0:
            self.head = new_node
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
        self.size += 1

    def popFront(self):
        # head 노드의 값 리턴. empty list이면 None 리턴
        if self.size == 0:
            return None
        else:
            popHead = self.head
            key = popHead.key
            self.head = popHead.next
            self.size -= 1
            del popHead

            return key

    def popBack(self):
        # tail 노드의 값 리턴. empty list이면 None 리턴
        if self.size == 0:
            return None
        else:
            prev = None
            tail = self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            if prev == None:
                self.head = None
            else:
                prev.next = tail.next
            key = tail.key
            del tail
            self.size -= 1
            return key

    def search(self, key):
        # key 값을 저장된 노드 리턴. 없으면 None 리턴
        v = self.head
        while v != None:
            if(v.key == key):
                return v
            v = v.next
        return None

    def remove(self, x):
        # 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
        if self.size == 0 or x == None:
            return False
        else:
            if x == self.head:
                self.popFront()
            else:
                prev = None
                target = self.head
                while target != x:
                    prev = target
                    target = target.next
                prev.next = target.next
                del target
                self.size -= 1
            return True

    def reverse(self, key):
        if self.search(key) == None:
            return

        # k = 1
        # start = self.head
        # while start != None:
        #     if(start.key == key):
        #         break
        #     start = start.next
        #     k += 1
        # for _ in range(self.size - k):
        #     tail = self.popBack()
        #     self.insert(k, tail)
        linkPoint = None
        start = self.head
        while start.next != None:
            if start.key == key:
                break
            linkPoint = start
            start = start.next

        prev = None
        while start != None:
            next = start.next
            start.next = prev
            prev = start
            start = next

        if linkPoint == None:
            self.head = prev
        else:
            linkPoint.next = prev

    def findMax(self):
        # self가 empty이면 None, 아니면 max key 리턴
        if self.size == 0:
            return None
        else:

            prev = None
            tail = self.head
            maxVal = tail.key
            while tail.next != None:
                prev = tail
                tail = tail.next
                if maxVal < tail.key:
                    maxVal = tail.key

            if prev == None:
                return maxVal
            else:
                if maxVal < tail.key:
                    maxVal = tail.key
                    return maxVal
                else:
                    return maxVal

    def deleteMax(self):
        # self가 empty이면 None, 아니면 max key 지운 후, max key 리턴
        if self.size == 0:
            return None
        else:
            key = self.findMax()
            maxNode = self.search(key)
            self.remove(maxNode)
            return key

    def insert(self, k, val):
        new_node = Node(val)
        if self.size < k:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
            self.size += 1
        else:
            count = 1
            v = self.head
            while v != None:
                if(count == k):
                    new_node.next = v.next
                    v.next = new_node
                    self.size += 1
                    return True
                v = v.next
                count += 1

    def size(self):
        return self.size


L = SinglyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == "pushFront":
        L.pushFront(int(cmd[1]))
        print(int(cmd[1]), "is pushed at front.")
    elif cmd[0] == "pushBack":
        L.pushBack(int(cmd[1]))
        print(int(cmd[1]), "is pushed at back.")
    elif cmd[0] == "popFront":
        x = L.popFront()
        if x == None:
            print("List is empty.")
        else:
            print(x, "is popped from front.")
    elif cmd[0] == "popBack":
        x = L.popBack()
        if x == None:
            print("List is empty.")
        else:
            print(x, "is popped from back.")
    elif cmd[0] == "search":
        x = L.search(int(cmd[1]))
        if x == None:
            print(int(cmd[1]), "is not found!")
        else:
            print(int(cmd[1]), "is found!")
    elif cmd[0] == "remove":
        x = L.search(int(cmd[1]))
        if L.remove(x):
            print(x.key, "is removed.")
        else:
            print("Key is not removed for some reason.")
    elif cmd[0] == "reverse":
        L.reverse(int(cmd[1]))
    elif cmd[0] == "findMax":
        m = L.findMax()
        if m == None:
            print("Empty list!")
        else:
            print("Max key is", m)
    elif cmd[0] == "deleteMax":
        m = L.deleteMax()
        if m == None:
            print("Empty list!")
        else:
            print("Max key", m, "is deleted.")
    elif cmd[0] == "insert":
        L.insert(int(cmd[1]), int(cmd[2]))
        print(cmd[2], "is inserted at", cmd[1]+"-th position.")
    elif cmd[0] == "printList":
        L.printList()
    elif cmd[0] == "size":
        print("list has", len(L), "nodes.")
    elif cmd[0] == "exit":
        print("DONE!")
        break
    else:
        print("Not allowed operation! Enter a legal one!")
