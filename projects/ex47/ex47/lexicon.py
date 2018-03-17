directions = ['north','south','east','west','down','up','left','right','back']
verbs = ['go','stop','kill','eat']
stops = ['the','in','of','from','at','it']
nouns = ['door','bear','princess','cabinet']

def scan(input_str):
    words = input_str.split()
    result = []
    for item in words:
        result.append(convert(item))
    return result


def convert(word):
    if word in directions:
        return ('direction',word)
    elif word in verbs:
        return ('verb', word)
    elif word in stops:
        return ('stop', word)
    elif word in nouns:
        return ('noun', word)
    elif convert_number(word):
        return ('number', int(word))
    else:
        return ('error', word)


def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
