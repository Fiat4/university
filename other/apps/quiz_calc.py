import random

MAX = 10
MIN = -10


class Action:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __call__(self) -> int:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError


class Sum(Action):
    def __repr__(self) -> str:
        return f"{self.x}{'+' if self.y >= 0 else ''}{self.y}"

    def __call__(self) -> int:
        return self.x + self.y


class Multiply(Action):
    def __repr__(self) -> str:
        return f"{self.x}{'*'}{self.y}"

    def __call__(self) -> int:
        return self.x * self.y


class Div(Action):
    def __repr__(self) -> str:
        return f"{self.x}//{self.y}"

    def __call__(self) -> int:
        return self.x // self.y


actions = [Sum, Multiply, Div]

lives = 3
count = 0

while lives > 0:
    action = random.choice(actions)
    task = action(random.randint(MIN, MAX), random.randint(MIN, MAX))
    print("Решите пример:", task)
    if int(input("Ответ: ")) == task():
        count += 1
    else:
        lives -= 1

print("Игра окончена! Кол-во правильно решенных примеров:", count)
