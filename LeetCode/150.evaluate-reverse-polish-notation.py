
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)  # Integer division
        }

        for token in tokens:
            if token in operators:
                b, a = stack.pop(), stack.pop()
                stack.append(operators[token](a, b))
            else:
                stack.append(int(token))

        return stack[0]


# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         def isNum(token: str):
#             ops = set()
#             ops.add('+')
#             ops.add('-')
#             ops.add('*')
#             ops.add('/')
#             return token not in ops
        
#         i = 0
#         while len(tokens) >= 3:
#             newCalculatedNum = float('inf')
#             segmentStart = i
#             segmentEnd = i + 2
#             threeTokens = tokens[segmentStart:segmentEnd + 1]
#             isTheFirstTokenValid = isNum(threeTokens[0])
#             isTheSecondTokenValid = isNum(threeTokens[1])
#             isTheThirdTokenValid = not isNum(threeTokens[2])
            
#             if isTheFirstTokenValid and isTheSecondTokenValid and isTheThirdTokenValid:
#                 if threeTokens[2]  == "+":
#                     newCalculatedNum = int(threeTokens[0]) + int(threeTokens[1])
#                 elif threeTokens[2]  == "-":
#                     newCalculatedNum = int(threeTokens[0]) - int(threeTokens[1])
#                 elif threeTokens[2]  == "*":
#                     newCalculatedNum = int(threeTokens[0]) * int(threeTokens[1])
#                 elif threeTokens[2]  == "/":
#                     newCalculatedNum = int(threeTokens[0]) / int(threeTokens[1])
#                 tokens = tokens[:segmentStart] + [newCalculatedNum] + tokens[segmentEnd+1:]
#                 i = max(0, i - 1)
#             else:
#                 i += 1
#         return int(tokens[0])
    

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.prev = None
#         self.next = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = self.tail = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node

#     def remove_node(self, node):
#         if node.prev:
#             node.prev.next = node.next
#         if node.next:
#             node.next.prev = node.prev
#         if node == self.head:
#             self.head = node.next
#         if node == self.tail:
#             self.tail = node.prev

#     def insert_after(self, node, value):
#         new_node = Node(value)
#         new_node.prev = node
#         new_node.next = node.next
#         if node.next:
#             node.next.prev = new_node
#         node.next = new_node
#         if node == self.tail:
#             self.tail = new_node

#     def convert_to_list(self):
#         result = []
#         current = self.head
#         while current:
#             result.append(current.value)
#             current = current.next
#         return result

# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         def isNum(token: str):
#             ops = {"+", "-", "*", "/"}
#             return token not in ops
        
#         # Convert the list of tokens to a doubly linked list
#         linked_list = DoublyLinkedList()
#         for token in tokens:
#             linked_list.append(token)

#         current = linked_list.head
#         while current and current.next and current.next.next:
#             first = current
#             second = current.next
#             third = current.next.next

#             isFirstValid = isNum(first.value)
#             isSecondValid = isNum(second.value)
#             isThirdValid = not isNum(third.value)

#             if isFirstValid and isSecondValid and isThirdValid:
#                 # Perform the calculation based on the operator
#                 a, b = int(first.value), int(second.value)
#                 if third.value == "+":
#                     result = a + b
#                 elif third.value == "-":
#                     result = a - b
#                 elif third.value == "*":
#                     result = a * b
#                 elif third.value == "/":
#                     result = int(a / b)  # Integer division

#                 # Modify the linked list
#                 third.value = result  # Replace the operator node with the result
#                 linked_list.remove_node(first)  # Remove the first number
#                 linked_list.remove_node(second)  # Remove the second number
                
#                 # Step back to recheck the new triplet
#                 current = third.prev if third.prev else third
#             else:
#                 current = current.next  # Move to the next node if no valid triplet is found

#         # The result is the only remaining node in the list
#         return int(linked_list.head.value)

