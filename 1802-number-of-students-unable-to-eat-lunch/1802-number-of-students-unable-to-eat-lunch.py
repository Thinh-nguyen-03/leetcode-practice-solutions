class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        students_queue = deque(students)
        sandwiches_stack = sandwiches
        unable_to_eat_count = 0

        while students_queue and sandwiches_stack:
            if students_queue[0] == sandwiches_stack[0]:
                students_queue.popleft()  # Student takes the sandwich
                sandwiches_stack.pop(0)  # Remove the top sandwich
                unable_to_eat_count = 0  # Reset the counter as a student has eaten
            else:
                students_queue.append(students_queue.popleft())  # Move student to the end of the queue
                unable_to_eat_count += 1

            if unable_to_eat_count == len(students_queue):
                break  # All remaining students cannot eat

        return len(students_queue)