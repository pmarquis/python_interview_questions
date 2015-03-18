def _negate(a):
    inc = -1 if a > 0 else 1
    val = 0
    while (val + a) != 0:
        val = val + inc
    return val


def _abs(a):
    return a if a > 0 else _negate(a)


def substract(a, b):
    return a + _negate(b)


def multiply(a, b):
    # algorithm is faster if a<b
    absa = _abs(a)
    absb = _abs(b)
    if absa > absb:
        return multiply(b, a)
    result = 0
    for i in range(absa):
        result = result + absb

    if (a >= 0 and b >= 0) or (a <= 0 and b <= 0):
        return result
    else:
        return _negate(result)


def divide(a, b):
    absa = _abs(a)
    absb = _abs(b)
    if b == 0:
        raise ValueError("b parameter should not be zero")
    result = 0
    product = 0
    while product + absb < absa:
        product = product + absb
        result = result + 1

    if (a >= 0 and b >= 0) or (a <= 0 and b <= 0):
        return result
    else:
        return _negate(result)
