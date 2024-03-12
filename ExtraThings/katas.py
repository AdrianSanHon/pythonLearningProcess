def sort_array(source_array):
    odd = {}
    odds = []
    i = 0

    resu = source_array
    while i < len(source_array):
        if(source_array[i] % 2 != 0):
            odd[i] = source_array[i]
            odds.append(source_array[i])
        i+=1

    odds = sorted(odds)
    keys = list(odd.keys())
    i = 0
    while i<len(odds):
        resu[keys[i]] = odds[i]
        i+=1
    return resu