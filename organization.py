import random


def getINN() -> str:
    inn = [str(random.randint(0, 9)) for i in range(9)]

    summ = 2 * int(inn[0]) + 4 * int(inn[1]) + 10 * int(inn[2]) + 3 * int(inn[3]) + 5 * int(inn[4]) + 9 * int(
        inn[5]) + 4 * int(inn[6]) + 6 * int(inn[7]) + 8 * int(inn[8])

    delenie = summ // 11
    summ2 = delenie * 11

    control = summ - summ2

    if control <= 9:
        control = control
    else:
        control = control % 10
    inn.append(str(control))
    return "".join(inn)


def getAcc(bic: str = '044525225') -> str:
    acc = list("40817810"[:]) + [str(random.randint(0, 9)) for j in range(12)]

    acc[8] = 0

    acc = list(bic[6:]) + acc

    mod = [7, 1, 3]

    controlsumm = 0
    print(acc)

    for i in range(len(acc)):
        controlsumm += int(acc[i]) * mod[i % 3] % 10

    return ''.join(acc[3:11] + [str(controlsumm * 3 % 10)] + acc[12:])

