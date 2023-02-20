import re
from random import randint

CPF_RE = re.compile(r"^\d{3}.\d{3}.\d{3}-\d{2}$")

__all__ = ["CPF_RE", "is_cpf", "formatted_cpf"]


def only_digits(num):
    return [int(n) for n in re.findall(r"\d", num)]


def calc_digit(num):
    weigth = (
        list(range(2, 11))[::-1] if len(num) == 9 else list(range(2, 12))[::-1]
    )
    get_sum = sum([num[i] * weigth[i] for i in range(len(num))])
    total = 11 - (get_sum % 11)
    return 0 if total > 9 else total


def is_cpf(num):
    cpf = only_digits(num)
    if not cpf or len(cpf) != 11 or cpf == [cpf[0] for i in range(11)]:
        return False
    if cpf[9] != calc_digit(cpf[0:9]):
        return False
    if cpf[10] != calc_digit(cpf[0:10]):
        return False
    return True


def fake_cpf():
    numbers = [randint(0, 9) for i in range(9)]
    for _ in range(2):
        numbers.append(calc_digit(numbers))
    return "".join([str(n) for n in numbers])


def formatted_cpf(num=False):
    if num:
        if is_cpf(num):
            cpf = "".join([str(n) for n in only_digits(num)])
        else:
            return "Enter a valid CPF"
    else:
        cpf = fake_cpf()
    return f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
