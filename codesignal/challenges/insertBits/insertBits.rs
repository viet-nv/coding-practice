fn insertBits(n: i32, a: i32, b: i32, k: i32) -> i32 {
    let m = (1 << b - a + 1) - 1;
    let x = n & !(m << a);
    return x | (k<<a);
}

