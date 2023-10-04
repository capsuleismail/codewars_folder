def fake_bin(x):
    result = ''
    bbl = {
        '0':'0',
        '1':'0',
        '2':'0',
        '3':'0',
        '4':'0',
        '5':'1',
       '6':'1',
        '7':'1',
        '8':'1',
        '9':'1'
    }
    for i in range(len(x)):
        result += bbl.get(x[i])
    return result