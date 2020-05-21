let insertBits = (n, a, b, k) =>
  (n & ~(((1 << (b - a + 1)) - 1) << a)) | (k << a);
