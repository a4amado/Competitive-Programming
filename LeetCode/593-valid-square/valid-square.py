class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # Helper function to calculate distance between two points
        def distance(point1, point2):
            return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2
        
        # If any points are the same, it's not a valid square
        if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4:
            return False
        
        # Calculate all possible distances between points
        distances = [
            distance(p1, p2),
            distance(p1, p3),
            distance(p1, p4),
            distance(p2, p3),
            distance(p2, p4),
            distance(p3, p4)
        ]
        
        # Sort distances to group sides and diagonals
        distances.sort()
        
        # For a valid square:
        # - First 4 distances should be equal (sides)
        # - Last 2 distances should be equal (diagonals)
        # - Diagonals should be larger than sides
        return (
            distances[0] > 0 and
            distances[0] == distances[1] == distances[2] == distances[3] and
            distances[4] == distances[5] and
            distances[4] > distances[0]
        )