def bin_to_decimal(inp):
    total = 0
    list_input = list(map(int, list(inp)))
    length = len(list_input)
    ind = -1
    while length:
        ind += 1
        length -= 1

        total += 2**length * list_input[ind]
    return total
