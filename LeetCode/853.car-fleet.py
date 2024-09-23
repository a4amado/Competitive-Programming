class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each position with its corresponding speed and sort in descending order of position
        pairs = sorted(zip(position, speed), reverse=True)
        
        times = []
        for pos, spd in pairs:
            # Calculate the time to reach the target for the current car
            time = (target - pos) / spd
            times.append(time)
        
        fleets = 0
        max_time = 0
        for time in times:
            if time > max_time:
                fleets += 1
                max_time = time
        
        return fleets