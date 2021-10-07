from dataclasses import dataclass

@dataclass
class ValueObject(object):
    context: str
    fname: str
    bugs: object
    melon: object
    train: object
    test: object
    id: str
    label: str

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> str: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> str: return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, label): self._label = label

    @property
    def bugs(self) -> str: return self._bugs

    @bugs.setter
    def bugs(self, bugs): self._bugs = bugs

    @property
    def melon(self) -> str: return self._melon

    @melon.setter
    def melon(self, melon): self._melon = melon

'''
출처: https://wikidocs.net/21053
파이썬에서 class을 지원하기 때문에 setter/getter 또한 지원한다. 
기본적으로 다음과 같이 구현할 수 있다. 
메서드에 set 혹은 get을 붙이면 된다.
class Car:
    def __init__(self, t):
        self.horsepower = t
    def gethorsepower(self):        # getter
        return self.horsepower
    def sethorsepower(self, str):   # setter
        self.horsepower = str
하지만 이렇게 하면 car.sethorsepower()에 직접 값을 넣을 수도 있고 
car.gethorsepower()를 직접 사용할 수도 있다. 
즉, 은닉되지 않는다. 
파이썬에는 private 혹은 public과 같은 예약어가 없기 때문이다. 
따라서 메서드를 은닉하기 위해 다음과 같이 한다.
출처: https://en.wikipedia.org/wiki/Value_object
In computer science, a value object is a small object that represents a simple entity
'''