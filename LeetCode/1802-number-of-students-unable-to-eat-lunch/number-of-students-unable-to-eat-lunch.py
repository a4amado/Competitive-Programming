#
# @lc app=leetcode id=1700 lang=python3
#
# [1700] Number of Students Unable to Eat Lunch
#

from typing import *
from collections import deque

# @lc code=start
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_q: Deque[int] = deque(students)
        
        sandwiches_q: Deque[int] = deque(sandwiches)
        

        
        number_of_sanwitches = len(sandwiches_q)

        while True:
            tries = 0
            number_of_sandwitches_taken_during_this_tuen = 0
            while tries != number_of_sanwitches and students_q:
                tries += 1
                first_sandwitch = sandwiches_q.popleft()
                first_student = students_q.popleft()
                if first_sandwitch == first_student:
                    number_of_sandwitches_taken_during_this_tuen += 1
                    continue
                else:
                    sandwiches_q.appendleft(first_sandwitch)
                    students_q.append(first_student)

            if not students_q: return 0
            number_of_sanwitches = len(sandwiches_q)
            if number_of_sandwitches_taken_during_this_tuen == 0:return len(students_q)