from icecream import ic


class Calculator(object):
    def __init__(self, num1, num2, opcode):
        self.num1 = num1
        self.num2 = num2
        self.opcode = opcode

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiple(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

    def remind(self):
        return self.num1 % self.num2

    @staticmethod
    def main():
        while 1:
            menu = input('0. Exit\t1. Calculate\n')
            if menu == '0':
                return
            elif menu == '1':
                num1 = int(input('First number : '))
                opcode = input('Opcode :')
                num2 = int(input('Second number : '))
                result = 0
                calc = Calculator(num1, num2, opcode)
                ic('*' * 100)
                if opcode == '+':
                    result = calc.add()
                elif opcode == '-':
                    result = calc.subtract()
                elif opcode == '*':
                    result = calc.multiple()
                elif opcode == '/':
                    result = calc.divide()
                elif opcode == '%':
                    result = calc.remind()
                ic(f'{calc.num1} {calc.opcode} {calc.num2} = {result}')
                ic('*' * 100)
            else:
                ic('Wrong Selected Number')