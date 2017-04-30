#! python3

directions = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verbs = ('go', 'stop', 'kill', 'eat', 'open')
stop_words = ('the', 'in', 'of', 'from', 'at', 'it')
nouns = ('door', 'bear', 'princess', 'cabinet')


def get_tuple(word):
    lowercase = word.lower()

    if lowercase in directions:
        return 'direction', word
    elif lowercase in verbs:
        return 'verb', word
    elif lowercase in stop_words:
        return 'stop', word
    elif lowercase in nouns:
        return 'noun', word
    elif lowercase.isdigit():
        return 'number', int(word)
    else:
        return 'error', word


def scan(sentence):
    words = sentence.split()
    return [get_tuple(word) for word in words]
