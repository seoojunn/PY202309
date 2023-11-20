class Student:
    def __init__(self, name, korean, math, english):
        # 학생의 이름, 국어, 수학, 영어 점수를 초기화
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english

    def get_average(self):
        #파일에서 읽어온 점수의 평균 구하는 함수
        scores = [self.korean, self.math, self.english]
        return sum(scores) /3