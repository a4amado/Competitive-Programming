
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # If amount is 0, no coins are needed
        if amount == 0:
            return 0
        
        coins.sort(reverse=True)
 
        # Initialize the queue with the starting amount 0 and 0 coins used
        queue = deque([(0, 0)])  # (current amount, number of coins)
        visited = set()  # To track visited amounts
        visited = {0:0}
        
        while queue:
            curr_amount, num_coins = queue.popleft()
            
            for coin in coins:
                newAmount = curr_amount + coin
                if newAmount == amount:
                    return num_coins + 1
                
                if newAmount > amount:
                    continue

                if newAmount not in visited or num_coins + 1 < visited[newAmount]:
                    visited[newAmount] = num_coins + 1
                    queue.append((newAmount, num_coins + 1))
                
                
                
            
        
        # If we exit the loop without returning, the amount cannot be formed
        return -1
