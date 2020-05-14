fn sum_digit(n: i32) -> i32 {
    let s = n.to_string();
    let mut sum = 0;
    for i in 0..s.len() {
        let x = &s[i..i+1];
        sum += x.parse::<i32>().unwrap();
    }
    return sum;
}

fn most_frequent(v: Vec<i32>) -> i32 {
    let mut result = v[0];
    let mut count = 0;
    for num in v.iter() {
        let current_frequency = v.iter().filter(|&n| *n == *num).count();
        if current_frequency > count {
            result = *num;
            count = current_frequency;
        }
    }
    return result;
}

fn mostFrequentDigitSum(n: i32) -> i32 {
    let mut s = vec![sum_digit(n)];
    let mut m = n;
    while m > 0 {
        let temp = m - sum_digit(m);
        s.push(sum_digit(temp));
        m = temp;
    }
    s.sort();
    s.reverse();
    return most_frequent(s);
}

