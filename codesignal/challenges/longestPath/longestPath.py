def longestPath(fileSystem):
    s = []
    curlen = 0
    maxlen = 0
    fileSystem = fileSystem.splitlines()
    for f in fileSystem:
        name = f.lstrip('\t')
        # level
        l = (len(f) - len(name))
        if s:
            for _ in range(len(s)-l):
                s.pop()

        s.append(name)
        curlen = sum([len(x) for x in s]) + len(s)-1
        if '.' in name and curlen > maxlen:
            maxlen = curlen

    return maxlen
