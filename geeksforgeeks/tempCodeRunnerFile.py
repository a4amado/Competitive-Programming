n = 9
m = 10
edges=[[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
src=0

s = Solution()
print(
    s.shortestPath(edges, n, m, src)
)