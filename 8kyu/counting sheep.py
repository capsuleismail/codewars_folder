def count_sheeps(sheep):
    answer = 0
    for i in range(len(sheep)):
        if sheep[i] == True:
            answer += 1
    return answer