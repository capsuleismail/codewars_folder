def flick_switch(lst):

    result = []
    boolean = True
    for i in range(len(lst)):
        if lst[i] == 'flick':
            boolean = not boolean
        result.append(boolean)
            
    return result