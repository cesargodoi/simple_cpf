from simple_cpf.simple_cpf import CPF_RE, CPF


def test_emptyvalue_is_an_invalid_cpf():
    assert CPF.is_valid("") is False


def test_11_same_digits_is_an_invalid_cpf():
    assert CPF.is_valid("00000000000") is False


def test_formated_11_same_digits_is_an_invalid_cpf():
    assert CPF.is_valid("111.111.111-11") is False


def test_nonumbercpf_is_an_invalid_cpf():
    assert CPF.is_valid("nonumbercpf") is False


def test_less_than_11_digits_is_an_invalid_cpf():
    assert CPF.is_valid("8945065482") is False


def test_formated_less_than_11_digits_is_an_invalid_cpf():
    assert CPF.is_valid("405.925.828-8") is False


def test_more_than_11_digits_is_an_invalid_cpf():
    assert CPF.is_valid("435087628661") is False


def test_formated_more_than_11_digits_is_an_invalid_cpf():
    assert CPF.is_valid("023.515.379-634") is False


def test_023_515_379_63_is_a_valid_cpf():
    assert CPF.is_valid("023.515.379-63") is True


def test_405_925_828_82_is_an_invalid_cpf():
    assert CPF.is_valid("405.925.828-82") is False


def test_43508762866_is_a_valid_cpf():
    assert CPF.is_valid("43508762866") is True


def test_89450654823_is_an_invalid_cpf():
    assert CPF.is_valid("89450654823") is False


def test_formatted_cpf():
    cpf = CPF.fake()
    assert CPF_RE.findall(cpf)[0] == cpf


def test_formatted_cpf_by_number():
    cpf = CPF.formatted("03840786568")
    assert CPF_RE.findall(cpf)[0] == cpf


def test_formatted_cpf_by_a_formatted_number():
    cpf = CPF.formatted("038.407.865-68")
    assert CPF_RE.findall(cpf)[0] == cpf
