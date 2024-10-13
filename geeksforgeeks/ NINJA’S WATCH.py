


from typing import List

def ninjaWatch(time: str) -> str:
    digits = [x for x in time.replace(":", "")]  # Extract digits
    
    def dfs(idx: int, curr: List[str], full: List[str]):
        if len(curr) == 4:
            hour = int("".join(curr[:2]))  # First two digits for hours
            minute = int("".join(curr[2:]))  # Last two digits for minutes
            if 0 <= hour <= 23 and 0 <= minute <= 59:
                full.append("".join(curr))  # Add valid time to result
            return
        
        if idx == 0:  # First hour digit
            for i in digits:
                if 0 <= int(i) <= 2:  # Hour can start with 0, 1, or 2
                    curr.append(i)
                    dfs(idx + 1, curr, full)
                    curr.pop()
        
        elif idx == 1:  # Second hour digit
            if curr[0] == "2":  # If first hour digit is 2, restrict second to 0-3
                for i in digits:
                    if 0 <= int(i) <= 3:
                        curr.append(i)
                        dfs(idx + 1, curr, full)
                        curr.pop()
            else:  # Otherwise, second hour digit can be 0-9
                for i in digits:
                    curr.append(i)
                    dfs(idx + 1, curr, full)
                    curr.pop()
        
        elif idx == 2:  # First minute digit
            for i in digits:
                if 0 <= int(i) <= 5:  # First minute digit must be 0-5
                    curr.append(i)
                    dfs(idx + 1, curr, full)
                    curr.pop()
        
        elif idx == 3:  # Second minute digit
            for i in digits:
                curr.append(i)  # Any digit can go here
                dfs(idx + 1, curr, full)
                curr.pop()

    l = []
    dfs(0, [], l)
    l.sort(key=lambda x: int(x))  # Sort the list of times numerically

    compareTo = int("".join(digits))  # Convert current time to integer for comparison
    for word in l:  # Find the next time larger than the current one
        if int(word) > compareTo:
            ll = []
            for idx, char in enumerate(word):
                if idx == 2:
                    ll.append(":")
                ll.append(char)
            return "".join(ll)

    # If no larger time found, return the smallest time from the sorted list
    ll = []
    for idx, char in enumerate(l[0]):
        if idx == 2:
            ll.append(":")
        ll.append(char)
    return "".join(ll)
