## Problems: [insertBits](https://app.codesignal.com/challenge/W9MciLfzQn6MDEG4D)
Given an integer `n`, replace its bits starting from the bit at position `a` to the bit at position `b`, inclusive, with the bits of integer `k`. Count from the least significant bit to the most significant bit, starting from `0`.

<br/>

### Example

* For `n = 1024`, `a = 1`, `b = 6`, and `k = 17`, the output should be <br/>
`insertBits(n, a, b, k) = 1058`.
<br />
`n = 100 0000 0000`, `k = 1 0001`, `1058 = 100 0010 0010`.
<br />

## Solution:
- Replace all bits from `a` to `b` in `n` by `0`: <br />
     + Create mask have `b - a + 1` bit `1`: `mask = 1 << (b - a + 1)  - 1`<br />
     + shift left mask `a` position: `mask = mask << a`<br />
     + replace all bits from `a` to `b` in `n` by `0`: `n = n & ~mask`<br />
- Get result: `n | (k << a)`

