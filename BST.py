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
        return v

    def deleteByMerging(self, x):
        if x == None:
            return None

        a, b, pt = x.left, x.right, x.parent

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

        else:
            if pt == None:
                self.root = None
            else:
                if pt.left == x:
                    pt.left = None
                else:
                    pt.right = None

    def height(self, x):  # 노드 x의 height 값을 리턴
        if x == None:
            return -1
        else:
            return self.findHeight(x)

    def findHeight(self, x):
        if x == None:
            return -1

        leftHeight = self.findHeight(x.left)
        rightHeight = self.findHeight(x.right)

        if leftHeight > rightHeight:
            return leftHeight + 1
        else:
            return rightHeight + 1

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


T = BST()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'deleteC':
        v = T.search(int(cmd[1]))
        T.deleteByCopying(v)
        print("- {0} is deleted by copying".format(int(cmd[1])))
    elif cmd[0] == 'deleteM':
        v = T.search(int(cmd[1]))
        T.deleteByMerging(v)
        print("- {0} is deleted by merging".format(int(cmd[1])))
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
    elif cmd[0] == 'Rleft':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateLeft(v)
            print("@ Rotated left at node {0}".format(cmd[1]))
    elif cmd[0] == 'Rright':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateRight(v)
            print("@ Rotated right at node {0}".format(cmd[1]))
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
