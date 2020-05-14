def mostFrequentDigitSum(n):
    r = [sum_digit(n)]
    while n > 0:
        x = n - sum_digit(n)
        r.append(sum_digit(x))
        n = x

    r = sorted(r)
    return most_frequent(r[::-1])

def sum_digit(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s


def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i

    return num
