from .check_cpf import check_cpf


def test_emptyvalue_is_an_invalid_cpf():
    assert check_cpf("") is False


def test_11_same_digits_is_an_invalid_cpf():
    assert check_cpf("00000000000") is False


def test_formated_11_same_digits_is_an_invalid_cpf():
    assert check_cpf("111.111.111-11") is False


def test_nonumbercpf_is_an_invalid_cpf():
    assert check_cpf("nonumbercpf") is False


def test_less_than_11_digits_is_an_invalid_cpf():
    assert check_cpf("8945065482") is False


def test_formated_less_than_11_digits_is_an_invalid_cpf():
    assert check_cpf("405.925.828-8") is False


def test_more_than_11_digits_is_an_invalid_cpf():
    assert check_cpf("435087628661") is False


def test_formated_more_than_11_digits_is_an_invalid_cpf():
    assert check_cpf("023.515.379-634") is False


def test_023_515_379_63_is_a_valid_cpf():
    assert check_cpf("023.515.379-63") is True


def test_405_925_828_82_is_an_invalid_cpf():
    assert check_cpf("405.925.828-82") is False


def test_43508762866_is_a_valid_cpf():
    assert check_cpf("43508762866") is True


def test_89450654823_is_an_invalid_cpf():
    assert check_cpf("89450654823") is False
    