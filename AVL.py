class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
        self.height = 0

    def __str__(self):
        return str(self.key)


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def preorder(self, v):
        if v:
            print(v.key, end=" ")
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):
        if v:
            self.inorder(v.left)
            print(v.key, end=" ")
            self.inorder(v.right)

    def postorder(self, v):
        if v:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=" ")

    def find_loc(self, key):
        if self.size == 0:
            return None
        p = None
        v = self.root
        while v:
            if v.key == key:
                return v
            else:
                if v.key < key:
                    p = v
                    v = v.right
                else:
                    p = v
                    v = v.left
        return p

    def search(self, key):
        p = self.find_loc(key)
        if p and p.key == key:
            return p
        else:
            return None

    def insert(self, key):
        v = Node(key)
        if self.size == 0:
            self.root = v
        else:
            p = self.find_loc(key)
            if p and p.key != key:
                if p.key < key:
                    p.right = v

                else:
                    p.left = v
                v.parent = p

        self.size += 1
        self.findHeight(v)
        return v

    def deleteByMerging(self, x):
        if x == None:
            return None

        a, b, pt = x.left, x.right, x.parent
        m = None
        if a == None:
            c = b
        else:
            c = m = a
            while m.right:
                m = m.right
            m.right = b
            if b:
                b.parent = m

        if self.root == x:
            if c:
                c.parent = None
            self.root = c
        else:
            if pt.left == x:
                pt.left = c
            else:
                pt.right = c
            if c:
                c.parent = pt
        self.size -= 1
        if m != None:
            self.findHeight(m)
        else:
            self.findHeight(pt)

    def deleteByCopying(self, x):
        if x == None:
            return None

        pt, L, R = x.parent, x.left, x.right
        if L != None:
            y = x.left
            while y.right:
                y = y.right
            x.key = y.key
            if y.left:
                y.left.parent = y.parent
            if y.parent.left == y:
                y.parent.left = y.left
            else:
                y.parent.right = y.left
            self.findHeight(y.parent)

        elif L == None and R != None:
            y = R
            while y.left:
                y = y.left
            x.key = y.key
            if y.right:
                y.right.parent = y.parent
            if y.parent.left == y:
                y.parent.left = y.right
            else:
                y.parent.right = y.right
            self.findHeight(y.parent)

        else:
            if pt == None:
                self.root = None
            else:
                if pt.left == x:
                    pt.left = None
                else:
                    pt.right = None
                self.findHeight(pt)
        self.size -= 1
        return x

    def height(self, x):  # 노드 x의 height 값을 리턴
        if x == None:
            return -1
        else:
            return x.height

    def findHeight(self, x):
        while x != None:
            L, R = x.left, x.right
            if L == None and R == None:
                x.height = 0
            elif L == None and R != None:
                x.height = R.height + 1
            elif L != None and R == None:
                x.height = L.height + 1
            else:
                if L.height > R.height:
                    x.height = L.height + 1
                else:
                    x.height = R.height + 1
            x = x.parent

    def succ(self, x):  # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
        # x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴
        if x == None:
            return None

        if x.parent == None:
            if x.right == None:
                return None
            else:
                z = x.right
                while z.left != None:
                    z = z.left
                return z

        else:
            if x.parent.left == x:
                if x.right == None:
                    z = x.parent
                    return z
                else:
                    z = x.right
                    return z
            else:
                if x.right == None:
                    return None
                else:
                    z = x.right
                    return z

    def pred(self, x):  # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
        # x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴
        if x == None:
            return None

        if x.parent == None:
            if x.left == None:
                return None
            else:
                z = x.left
                while z.right != None:
                    z = z.right
                return z

        else:
            if x.parent.left == x:
                if x.left == None:
                    return None
                else:
                    z = x.left
                    return z
            else:
                if x.left == None:
                    z = x.parent
                    return z
                else:
                    z = x.left
                    while z != None:
                        z = z.right
                    return z

    def rotateLeft(self, x):  # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        if x == None:
            return
        z = x.right
        if z == None:
            return

        b = z.left
        z.parent = x.parent

        if x.parent != None:
            if x.parent.left == x:
                x.parent.left = z
            else:
                x.parent.right = z

        z.left = x
        x.parent = z
        x.right = b
        if b != None:
            b.parent = x
        if x == self.root:
            self.root = z
        self.findHeight(x)

    def rotateRight(self, x):  # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        if x == None:
            return

        z = x.left
        if z == None:
            return

        b = z.right
        z.parent = x.parent

        if x.parent != None:
            if x.parent.left == x:
                x.parent.left = z
            else:
                x.parent.right = z

        z.right = x
        x.parent = z
        x.left = b
        if b != None:
            b.parent = x
        if x == self.root:
            self.root = z
        self.findHeight(x)


class AVL(BST):
    def __init__(self):
        self.root = None
        self.size = 0

    def rebalance(self, x, y, z):
        # assure that x, y, z != None
        # return the new 'top' node after rotations
        # z - y - x의 경우(linear vs. triangle)에 따라 회전해서 균형잡음
        if z.left == y and y.left == x:
            super().rotateRight(z)
            w = y
        elif z.right == y and y.right == x:
            super().rotateLeft(z)
            w = y
        elif z.left == y and y.right == x:
            super().rotateLeft(y)
            super().rotateRight(z)
            w = x
        else:
            super().rotateRight(y)
            super().rotateLeft(z)
            w = x

        return w

    def insert(self, key):
        # BST에서도 같은 이름의 insert가 있으므로, BST의 insert 함수를 호출하려면
        # super(class_name, instance_name).method()으로 호출
        # 새로 삽입된 노드가 리턴됨에 유의!
        v = super(AVL, self).insert(key)
        # x, y, z를 찾아 rebalance(x, y, z)를 호출
        if self.root == v:
            return v
        else:
            pt = v.parent
            while pt != None:
                balanceFactor = abs(super().height(
                    pt.right) - super().height(pt.left))
                if balanceFactor == 2:
                    z = pt
                    if super().height(z.right) > super().height(z.left):
                        y = z.right
                    else:
                        y = z.left
                    if super().height(y.right) > super().height(y.left):
                        x = y.right
                    else:
                        x = y.left
                    w = self.rebalance(x, y, z)
                    if w.parent == None:
                        self.root = w
                    break
                pt = pt.parent

        return v

    def delete(self, u):  # delete the node u
        # 또는 self.deleteByMerging을 호출가능하다. 그러나 이 과제에서는 deleteByCopying으로 호출한다
        v = self.deleteByCopying(u)
        # height가 변경될 수 있는 가장 깊이 있는 노드를 리턴받아 v에 저장

        while v:
            balanceFactor = abs(super().height(
                v.right) - super().height(v.left))
            if balanceFactor == 2:
                z = v
                if super().height(z.left) >= super().height(z.right):
                    y = z.left
                else:
                    y = z.right
                if super().height(y.left) >= super().height(y.right):
                    x = y.left
                else:
                    x = y.right
                v = self.rebalance(x, y, z)
            w = v

            # v가 AVL 높이조건을 만족하는지 보면서 루트 방향으로 이동
            # z - y - x를 정한 후, rebalance(x, y, z)을 호출
            v = v.parent
        self.root = w


T = AVL()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'delete':
        v = T.search(int(cmd[1]))
        T.delete(v)
        print("- {0} is deleted".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'height':
        h = T.height(T.search(int(cmd[1])))
        if h == -1:
            print("= {0} is not found!".format(cmd[1]))
        else:
            print("= {0} has height of {1}".format(cmd[1], h))
    elif cmd[0] == 'succ':
        v = T.succ(T.search(int(cmd[1])))
        if v == None:
            print("> {0} is not found or has no successor".format(cmd[1]))
        else:
            print("> {0}'s successor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'pred':
        v = T.pred(T.search(int(cmd[1])))
        if v == None:
            print("< {0} is not found or has no predecssor".format(cmd[1]))
        else:
            print("< {0}'s predecssor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
