from StudentModule import Student

lines = open("student.csv", "r", encoding="utf8").readlines()
students = []

for line in lines:
    tokens = line.strip().split(",")
    if len(tokens) >= 4:
        student_name = tokens[0]
        try:
             # 각각의 점수를 실수로 변환, 변환에 실패하면 무시
            korean = float(tokens[1])
            math = float(tokens[2])
            english = float(tokens[3])

            # Import 된 클래스 사용
            student = Student(student_name, korean, math, english)
            students.append(student)
        except ValueError:
            continue

print("-----학생들의 평균 점수------")
for student in students:
    average_score = student.get_average()
    if average_score is not None:
        print("{}의 평균 점수는 {} 입니다.".format(student.name, average_score))