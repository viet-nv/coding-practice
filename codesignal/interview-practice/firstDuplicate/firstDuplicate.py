def firstDuplicate(a):
    count = [0]*100001
    idx = [-1]*100001
    for  index, value in enumerate(a):
        count[value] += 1
        if count[value] == 2:
            idx[value] = index

    res = -1
    i = 100002

    for index, value in enumerate(count):
        if value >= 2 and i > idx[index]:
            res = index;
            i = idx[index]

    return res
