from icecream import ic
'''
이름, 나이, 주소를 입력받아서 자기 소개하는 프로그램을 작성하시오.
안녕하세요, 제 이름은 Tom이고, 나이는 28세이고, 서울에서 거주합니다.
이때, 여러 사람이면 전부 입력 받아서 전체가 일괄 출력되는 시스템
'''


class Person(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.people = []

    def to_string(self, param):
        return str(f'안녕하세요, 제 이름은 {param.name}이고, 나이는 {param.age}세 이고, {param.address}에서 거주합니다.')

    def addPerson(self, param):
        return self.people.append(param)

    @staticmethod
    def main():
        count = int(input("몇 명입니까?"))
        result = []
        for i in range(count):
            person = Person(input("이름은?"), input('나이는?'), input('주소는?'))
            result.append(person.to_string(person))
        for i in result:
            ic(i)

'''
이름, 나이, 주소를 입력받아서 자기 소개하는 프로그램을 작성하시오.
안녕하세요, 제 이름은 Tom이고, 나이는 28세이고, 서울에서 거주합니다.
이때, 여러 사람이면 전부 입력 받아서 전체가 일괄 출력되는 시스템
'''


class Person2(object):
    def __init__(self, num):
        self.num = num
        self.people = []
        self.introduce = []

    def addPerson(self, info):
        return self.people.append(info)

    def addHi(self):
        return self.introduce.append(f'안녕하세요, 제 이름은 {self.people[-3]}이고, 나이는 {self.people[-2]}이고, {self.people[-1]}에 거주합니다.')

    def sayHi(self):
        for i in self.introduce:
            ic(i)

    @staticmethod
    def main():
        person = Person2(int(input("사람은 몇 명입니까?")))
        for j in range(person.num):
            for i in ['이름이 어떻게 됩니까?', '나이가 어떻게 됩니까?', '어디에 삽니까?']:
                person.addPerson(input(f'{i}'))
            person.addHi()
        person.sayHi()


class Person3(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def to_string(self):
        ic(f'name : {self.name} age : {self.age} address : {self.address}')

    @staticmethod
    def main():
        people = []
        while 1:
            menu = input('0 1 2 ')
            if menu == '0':
                return
            elif menu == '1':
                people.append(Person3(input('name : '), input('age : '), input('address :')))
            elif menu == '2':
                for i in people:
                    i.to_string()
