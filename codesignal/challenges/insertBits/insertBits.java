int insertBits(int n, int a, int b, int k) {
    int m = (1 << b - a + 1) - 1;
    int x = n & ~(m << a);
    return x | (k << a);
}

