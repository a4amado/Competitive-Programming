#
# @lc app=leetcode id=1311 lang=python3
#
# [1311] Get Watched Videos by Your Friends
#
from typing import *
from collections import deque, Counter
# @lc code=start
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        
        q = deque([])
        q.append([id, watchedVideos[id]])
        visited = {}
        visited[id] = True
        currLevel = 0
        
        while q and currLevel < level:
            newQ = deque([])
            while q:
                idx, _ = q.popleft()
                
                for nei in friends[idx]:
                    if nei not in visited:
                        visited[nei] = True
                        newQ.append([nei, watchedVideos[nei]])
                
            currLevel += 1
            q = newQ
        f = []
        for i in q:
            f += i[1]
        s = Counter(f)
        s = [[i, c] for c,i in s.items()]
        s.sort(key=lambda x: (x[0], x[1]))  # Sort by count (ascending) then alphabetically
        return [ss[1] for ss in s]



# @lc code=end
watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]]
id = 0
level = 1

s = Solution()

print(
    s.watchedVideosByFriends(watchedVideos, friends, id, level)
)

watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]]
id = 0
level = 2

print(
    s.watchedVideosByFriends(watchedVideos, friends, id, level)
)


