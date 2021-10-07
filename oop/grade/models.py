from icecream import ic
'''
국어 kor, 영어 eng, 수학 math를 입력받아서
평균정수를 통해서 A-F 학점을 출력하시오
'''


class Grade(object):
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.sum()/3

    def score(self):
        if int(self.avg()) >= int('90'):
            return 'A'
        elif int(self.avg()) >= int('80'):
            return 'B'
        elif int(self.avg()) >= int('70'):
            return 'C'
        elif int(self.avg()) >= int('60'):
            return 'D'
        elif int(self.avg()) >= int('50'):
            return 'E'
        elif int(self.avg()) >= int('40'):
            return 'F'
        else:
            return 'Fail'

    @staticmethod
    def main():
        kor = int(input('국어 점수를 입력하세요 : '))
        eng = int(input('영어 점수를 입력하세요 : '))
        math = int(input('수학 점수를 입력하세요 : '))
        grade = Grade(kor, eng, math)
        ic(f'당신의 점수는 {grade.score()}입니다. ')


'''
국어 kor, 영어 eng, 수학 math를 입력받아서
평균정수를 통해서 A-F 학점을 출력하시오
'''


class GradeTest(object):
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    @staticmethod
    def main():
        kor = input('국어 점수를 입력하세요 : ')
        eng = input('영어 점수를 입력하세요 : ')
        math = input('수학 점수를 입력하세요 : ')
        grade = GradeTest(kor, eng, math)
        average = int((int(grade.kor) + int(grade.eng) + int(grade.math))/3)
        if int(average) >= int('90'):
            return ic('A')
        elif int(average) >= int('80'):
            return ic('B')
        elif int(average) >= int('70'):
            return ic('C')
        elif int(average) >= int('60'):
            return ic('D')
        elif int(average) >= int('50'):
            return ic('E')
        elif int(average) >= int('40'):
            return ic('F')
        else:
            return ic('Fail')


'''
국어 kor, 영어 eng, 수학 math를 입력받아서
평균정수를 통해서 A-F 학점을 출력하시오
학생 이름, 평균 점수 ,학점을 출력하시오
'''


class GradeWithName(object):
    def __init__(self, name):
        self.name = name
        self.scores = []

    def addScore(self, score):
        self.scores.append(score)

    def avg(self):
        return sum(self.scores) / len(self.scores)

    def result(self, avg):
        if int(avg) >= int('90'):
            return 'A'
        elif int(avg) >= int('80'):
            return 'B'
        elif int(avg) >= int('70'):
            return 'C'
        elif int(avg) >= int('60'):
            return 'D'
        elif int(avg) >= int('50'):
            return 'E'
        elif int(avg) >= int('40'):
            return 'F'
        else:
            return 'Fail'

    @staticmethod
    def main():
        people = []
        for j in [1, 2, 3]:
            grade = GradeWithName(input('성명을 입력하세요 : '))
            for i in ['Korean', 'English', 'Math', 'Science']:
                grade.addScore(int(input(f'{i} 점수를 입력하세요 : ')))
            people.append(f'[{grade.name}의 성적표] 평균 점수 : {grade.avg()}  학점 : {grade.result(grade.avg())}')

        for k in people:
            ic(k)


