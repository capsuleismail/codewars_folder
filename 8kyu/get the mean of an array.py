def get_average(marks):
    if len(set(marks)) == 1:
        return marks[0]
    sum = 0
    length = len(marks)
    for i in range(len(marks)):
        sum += marks[i]
    return sum//length