def permutations(s):
    # copilot solve
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [s]
    else:
        res = []
        for i in range(len(s)):
            rest = s[:i] + s[i+1:]
            for p in permutations(rest):
                res.append(s[i] + p)
        return list(set(res))
