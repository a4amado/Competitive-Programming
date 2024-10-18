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

        parents = {i: [] for i in range(n)}
        
        # Build parent-child relationships
        for i in range(len(l) - 1, -1, -1):
            if l[i] == -1: 
                continue
            parentIdx = (i - 1) // 2
            if parentIdx < 0: 
                continue
            parents[l[i]].append(l[parentIdx])

        # Count nodes with no parents and nodes with more than one parent
        # noParents = 0
        # moreThanOneParent = 0
        
        # for node in parents.values():
        #     if len(node) == 0:
        #         noParents += 1
        #     if len(node) > 1:
        #         moreThanOneParent += 1

        # # There should be exactly one root and no node should have more than one parent
        # if noParents != 1 or moreThanOneParent > 0:
        #     return False

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
