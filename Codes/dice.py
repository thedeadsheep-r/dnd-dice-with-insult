import random

def dice(y):
    return random.randint(1, y)


def multiRolls(y):
    x = 0
    for i in y:
        x = x + int(i)

    return x


def advantageRoll(y):
    roll1 = dice(y)
    roll2 = dice(y)
    result = max(roll1, roll2)

    return f"Rolls: {roll1} and {roll2}\nAdvantage: {result}"


def disadvantageRoll(y):
    roll1 = dice(y)
    roll2 = dice(y)
    result = min(roll1, roll2)

    return f"Rolls: {roll1} and {roll2}\nDisadvantage: {result}"


def modadvantageRoll(y,x):
    roll1 = dice(y)
    roll2 = dice(y)
    result = max(roll1, roll2)

    return f"Rolls: {roll1} and {roll2}\nAdvantage: {result} with Modifier {x} it will be {result + x}"