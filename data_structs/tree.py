from __future__ import annotations


class Tree:
    def __init__(self, data: any = None):
        self.left = None
        self.right = None
        self.data = data

    def get_data(self) -> any:
        return self.data

    def get_left(self) -> Tree:
        if self.left is not None:
            return Tree(self.left.get_data())

    def get_right(self) -> Tree:
        if self.right is not None:
            return Tree(self.right.get_data())

    def set_data(self, data: any) -> None:
        self.data = data

    def set_left(self, left: Tree) -> None:
        self.left = left

    def set_right(self, right: Tree) -> None:
        self.left = right
