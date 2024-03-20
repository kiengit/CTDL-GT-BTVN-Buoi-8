class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # implementation of the insert method

    def contains(self, target):
        temp = self.root
        while temp:
            if target == temp.value:
                return True
            elif target < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False
