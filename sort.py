def sort_dictionary(map: dict):
    arr = sorted(map.items(), key=lambda val: val[1][1])
    res = []
    for v in arr:
        res.append((v[0], v[1][0]))
    return res