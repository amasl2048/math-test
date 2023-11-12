from f_math import digits as dg

for i in range(100):
    res = dg(1)  #; print(res)
    assert(res > 1)
    assert(res < 10)

for i in range(1000):
    res = dg(2)  #; print(res)
    assert(res >= 10)
    assert(res < 100)
