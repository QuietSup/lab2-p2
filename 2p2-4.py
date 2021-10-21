class Node:
    """Contains a binary tree with info about product code and price"""
    def __init__(self, data):
        """Checks if entered data isn't empty and if it has the correct type

        :param data: info about product code and price
        :type data: tuple(int, int)
        """
        if not data:
            raise ValueError("empty data")
        if not isinstance(data, tuple):
            raise TypeError("data must be tuple")
        if not data[0] or not data[1]:
            raise ValueError("empty code number or price")
        if not isinstance(data[0], int) or not isinstance(data[1], int):
            raise TypeError("price and  must be tuple")
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """Inserts new data into the binary tree

        :param data: info about product code and price
        :type data: tuple(int, int)
        """
        if not self.data:
            raise Exception("Tree doesn't exist")

        if self.data == data:
            return

        if data[0] < self.data[0]:
            if self.left:
                self.left.insert(data)
                return
            self.left = Node(data)
            return

        if self.right:
            self.right.insert(data)
            return
        self.right = Node(data)

    def inorder(self, all_data=[]):
        """Traverses the tree
        :param all_data: collects the info while traversing the tree to return it
        :type all_data: list(int, int)
        """
        if self.left is not None:
            self.left.inorder(all_data)
        if self.data is not None:
            all_data.append(self.data)
        if self.right is not None:
            self.right.inorder(all_data)
        return all_data

    def findval(self, to_find):
        """Finds the value, if can't - raises an error"""
        if to_find < self.data[0]:
            if self.left is None:
                raise ValueError("No item with this product code found")
            return self.left.findval(to_find)
        elif to_find > self.data[0]:
            if self.right is None:
                raise ValueError("No item with this product code found")
            return self.right.findval(to_find)
        else:
            return self.data[1]


def printTree(node, level=0):
    """Draws a binary tree"""
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.data)
        printTree(node.right, level + 1)


x = Node((6, 87))
x.insert((7, 93))
x.insert((4, 34))
x.insert((5, 25))
x.insert((3, 65))
x.insert((8, 23))
x.insert((2, 71))
print(x.inorder())
code = 3  # int(input('Product code:'))
amount = 4  # int(input('Amount: '))
print(x.findval(code) * amount)
printTree(x)
