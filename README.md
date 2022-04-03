# pln_fx | Get Rates from the National Bank of Poland

So the ECB (European Central Bank) publishes PLN (Zloty) rates but for accounting purposes in Poland there is a requirement to use the rate directly from the Polish National Bank instead of the ECB. Therefore I wrote this library because I am sure other people will need this and I havent found any library. So I dit it.

# Links

[https://pypi.org/project/pln-fx/](https://pypi.org/project/pln-fx/)<br />
[https://github.com/stephansemerad/National-Bank-of-Poland-Rates](https://github.com/stephansemerad/National-Bank-of-Poland-Rates)

# Install

```bash
pip install pln-fx
```

# How To Use

```python
from pln_fx import PLN_FX
fx = PLN_FX()

year_rate = fx.get_year('2022')
print('\n year_rate: ', year_rate)

day_rate = fx.get_date('2022-01-03')
print('\n day_rate: ', day_rate)

```

![](https://raw.githubusercontent.com/stephansemerad/National-Bank-of-Poland-Rates/master/pln_fx/api.png)

![](https://raw.githubusercontent.com/stephansemerad/National-Bank-of-Poland-Rates/master/pln_fx/overview.png)
