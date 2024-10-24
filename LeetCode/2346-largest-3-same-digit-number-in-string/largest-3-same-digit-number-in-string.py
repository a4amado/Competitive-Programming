class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if len(num) < 3: return ""
        largest = float("-inf")
        for i in range(0, len(num) - 2):
            first = num[i]
            second = num[i+1]
            third = num[i+2]
            if ((first == second) and (second == third)):
                if largest == float('-inf') or int(largest) < int(num[i:i+3]):
                    largest = num[i:i+3]

        return str(largest) if largest != float('-inf') else ""
