def draw_stairs(n):
    res = ''
    for i in range(0, n-1):
        res += (' '*i)+'I'+'\n'
    return res+(' '*(n-1)+'I')