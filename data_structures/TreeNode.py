class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode(val={self.val}, left={repr(self.left)}, right={repr(self.right)})"

    def __str__(self):
        return self._to_str()

    def _to_str(self, level=0):
        ret = "    " * level + repr(self.val) + "\n"
        if self.left:
            ret += self.left._to_str(level + 1)
        if self.right:
            ret += self.right._to_str(level + 1)
        return ret
