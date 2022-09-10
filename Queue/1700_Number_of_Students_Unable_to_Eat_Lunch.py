def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    cntr_students = 0
    for x in sandwiches:
        while cntr_students < len(students):
            val = students.pop(0)

            if val == x:
                cntr_students = 0
                break
            else:
                cntr_students += 1
                students.append(val)

        if cntr_students == len(students):
            break
        else:
            continue

    return len(students)