def reverse_words(s):
    while s:
        sentence = s.split(' ')
        result = ' '.join(sentence[i] for i in range(len(sentence)-1, -1, -1))
        return result
    return s