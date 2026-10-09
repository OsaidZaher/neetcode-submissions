from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)

        skipped = 0

        while students:
            sandwich = sandwiches[0]
            student = students.popleft()

            if student == sandwich:
                sandwiches.popleft()
                skipped = 0
            else:
                students.append(student)
                skipped += 1

            if skipped == len(students):
                break

        return len(students)