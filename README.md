# Simple CPF

A simple package to validate and format the CPF - _Brazil Identification Card_.   

## Installation

```bash
pip install simple-cpf
```

## How to use

```python
import simple_cpf.simple_cpf import CPF

# validating a cpf
CPF.is_valid('117.762.459-11')  # True
CPF.is_valid('117.762.459-19')  # False

# generating a fake cpf
CPF.fake()                      # '917.350.558-75'

# formatting a valid cpf
CPF.formatted('10757246354')    # '107.572.463-54'
                                # in case of invalid cpf, it will return:
                                # 'Enter a valid CPF.'
```

## Made by:
cesargodoi  -  https://github.com/cesargodoi/simple_cpf