from typing import List

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = 0
        l = [0]
        idx = 0
        level = 1

        # Extend the l array with children
        while idx < n:
            end = min(idx + level, n)
            l.extend(leftChild[idx:end])
            l.extend(rightChild[idx:end])
            idx += level
            level *= 2
        
        # Detect unused node to consider as root (if possible)
        ll = set(l)
        for i in range(n):
            if i not in ll:
                l[0] = i
                break



        # Check for cycles using DFS
        visited = set()

        def dfs(node):
            if node in visited:
                return False  # Cycle detected
            visited.add(node)
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if not dfs(child):
                        return False
            return True

        # Ensure we start DFS from the root node (node with no parents)
        root = l[0]
        if not dfs(root):
            return False

        # Ensure all nodes are visited (fully connected)
        return len(visited) == n


# @lc code=end

n = 4
leftChild = [1,-1,3,-1]
rightChild = [2,3,-1,-1]
s = Solution()
print(
    s.validateBinaryTreeNodes(n,leftChild, rightChild)
)
n = 4
leftChild = [1,-1,3,-1]
rightChild = [2,-1,-1,-1]
print(
    s.validateBinaryTreeNodes(n,leftChild, rightChild)
)


n = 2
leftChild = [1,0]
rightChild = [-1,-1]

print(
    s.validateBinaryTreeNodes(n,leftChild, rightChild)
)

