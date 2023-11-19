'''
lines = open("student.csv","r", encoding="utf8").readlines()
# 학생 정보를 딕셔너리에 저장
student_info = {}  # 학생 정보를 저장할 딕셔너리
for line in lines:
    tokens = line.strip().split(",")  # 각 줄을 쉼표로 분할하여 학생 정보 추출
    if len(tokens) >= 4:  # 최소 토큰 개수를 확인
        student_name = tokens[0]
        student_scores = []
        for score in tokens:
            try:
                student_scores.append(float(score))  # 숫자로 변환 가능한 경우에만 점수를 실수로 변환하여 리스트에 추가
            except ValueError:
                continue  # 변환할 수 없는 경우, 해당 값 무시
        student_info[student_name] = student_scores
print("-----학생들의 평균 점수------")        
# 학생 별 평균 점수를 계산
for student, scores in student_info.items():
    if scores:  # 빈 리스트를 제외하고 계산
        average_score = sum(scores) / len(scores)
        print("{}의 평균 점수는 {} 입니다.".format(student,average_score))
#딕셔너리에 저장된 value에 접근해서 평균 계산
'''
class Student:
    def __init__(self, name, korean, math, english):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english

    def get_average(self):
        scores = [self.korean, self.math, self.english]
        return sum(scores) /3
lines = open("student.csv", "r", encoding="utf8").readlines()
students = []
for line in lines:
    tokens = line.strip().split(",")
    if len(tokens) >= 4:
        student_name = tokens[0]
        try:
            # Attempt to convert scores to float, ignore if conversion fails
            korean = float(tokens[1])
            math = float(tokens[2])
            english = float(tokens[3])

            # Create a Student instance and append it to the list
            student = Student(student_name, korean, math, english)
            students.append(student)
        except ValueError:
            continue

# Print average scores for each student
print("-----학생들의 평균 점수------")
for student in students:
    average_score = student.get_average()
    if average_score is not None:
        print("{}의 평균 점수는 {} 입니다.".format(student.name, average_score))

'''
#사진 아래(로드 데이터 안에)
std_ins=Student()
std_ins.name=tokens[0]
std_ins.korean=float(tokens[1])
std_ins.math=float(tokens[2])
std_ins.english=float(tokens[3])
student_list.append(std_ins)
return student_list

print(student_ins.get_average())
'''
