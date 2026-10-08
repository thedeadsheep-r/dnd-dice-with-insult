import dice

def error_fix(y):


    try:
        x = int(y)

    except ValueError:

        x = 1
        return x
    else:
        return int(y)

def multi(x,y):
    multi = x
    array_sum = []

    for i in range(multi):
            x = dice.dice(y)
            array_sum.append(x)

    a = dice.multiRolls(array_sum)

    array_sum.append(a)

    return array_sum
