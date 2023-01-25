n = int(input())
students = {}

for _ in range(n):
    student, grade = input().split()

    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for k, v in students.items():
    avg_grade = sum(v) / len(v)
    grades_in_row_as_string = ' '.join(map(lambda grade: f'{grade:.2f}', v))
    print(f"{k} -> {grades_in_row_as_string} (avg: {avg_grade:.2f})")