import re
from random import randint

CPF_RE = re.compile(r"^\d{3}.\d{3}.\d{3}-\d{2}$")


class CPF:
    def only_digits(num):
        return [int(n) for n in re.findall(r"\d", num)]

    def calc_digit(num):
        weigth = (
            list(range(2, 11))[::-1]
            if len(num) == 9
            else list(range(2, 12))[::-1]
        )
        get_sum = sum([num[i] * weigth[i] for i in range(len(num))])
        total = 11 - (get_sum % 11)
        return 0 if total > 9 else total

    @classmethod
    def is_valid(cls, num):
        cpf = cls.only_digits(num)
        if not cpf or len(cpf) != 11 or cpf == [cpf[0] for i in range(11)]:
            return False
        if cpf[9] != cls.calc_digit(cpf[0:9]):
            return False
        if cpf[10] != cls.calc_digit(cpf[0:10]):
            return False
        return True

    @classmethod
    def fake(cls):
        numbers = [randint(0, 9) for i in range(9)]
        for _ in range(2):
            numbers.append(cls.calc_digit(numbers))
        return cls.formatted("".join([str(n) for n in numbers]))

    @classmethod
    def formatted(cls, num):
        if cls.is_valid(num):
            cpf = "".join([str(n) for n in cls.only_digits(num)])
        else:
            return "Enter a valid CPF."
        return f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
