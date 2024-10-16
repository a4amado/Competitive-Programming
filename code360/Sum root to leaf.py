
from typing import List, Optional

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def rootToLeafSum(root: BinaryTreeNode):
    def backtracking(curr: Optional[BinaryTreeNode], path: List[int], all_paths: List[str]):
        if not curr:return
        path.append(str(curr.data))
        
        if not curr.left and not curr.right:
            all_paths.append("".join(path))
        else:
            backtracking(curr.left, path, all_paths)
            backtracking(curr.right, path, all_paths)

        path.pop()

    all_paths = []
    MOD = 10**9+7
    backtracking(root, [], all_paths)
    return sum(int(val) for val in all_paths) % MOD