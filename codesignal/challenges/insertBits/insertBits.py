# def insertBits(n, a, b, k):
#     mask = (1 << b - a + 1) - 1
#     m = n & ~(mask<<a)
#     return m | (k << a)

insertBits = lambda n, a, b, k: n & ~((1 << b - a + 1) - 1 << a) | k << a
