import re
from random import randint


def calc_digit(num):
    weigth = (
        list(range(2, 11))[::-1] if len(num) == 9 else list(range(2, 12))[::-1]
    )
    get_sum = sum([num[i] * weigth[i] for i in range(len(num))])
    total = 11 - (get_sum % 11)
    return 0 if total > 9 else total


def check_cpf(number):
    is_cpf = [int(n) for n in re.findall(r"\d", number)]
    if not is_cpf:
        return False
    elif is_cpf == [is_cpf[0] for i in range(11)]:
        return False
    elif len(is_cpf) != 11:
        return False

    if is_cpf[9] != calc_digit(is_cpf[0:9]):
        return False

    if is_cpf[10] != calc_digit(is_cpf[0:10]):
        return False

    return True


def generate_cpf():
    numbers = [randint(0, 9) for i in range(9)]
    for _ in range(2):
        numbers.append(calc_digit(numbers))
    return "".join([str(n) for n in numbers])


def formated_cpf(number=False):
    if number:
        if check_cpf(number):
            _cpf = [int(n) for n in re.findall(r"\d", number)]
            cpf = "".join([str(n) for n in _cpf])
        else:
            return "Enter a valid CPF"
    else:
        cpf = generate_cpf()
    return f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
