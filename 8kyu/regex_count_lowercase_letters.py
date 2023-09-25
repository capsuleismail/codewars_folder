#"abc" ===> 3
#"abcABC123" ===> 3
#"abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 3
#"" ===> 0;
#"ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 0
#"abcdefghijklmnopqrstuvwxyz" ===> 26
#solution
def lowercase_count(strng):
    count = 0
    for i in range(len(strng)):
        if strng[i].islower():
            count += 1
    return count