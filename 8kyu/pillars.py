def pillars(num_pill, dist, width):
    dist = dist*100
    if num_pill <= 1:
        return 0
    else:
        return (num_pill - 1) * dist + (width * (num_pill-2))
