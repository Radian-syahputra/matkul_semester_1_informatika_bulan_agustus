def two_sum (nums : list[int], target : int) -> list[int] :
    peta : dict[int, int] = {}
    for i, x in enumerate(nums) :
        sisa = target - x
        if sisa in peta :
            return[peta[sisa], i]
        peta[x] = i
    return []

    