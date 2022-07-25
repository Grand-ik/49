class Sentence(object):
    '''Creates a Sentence object, - a basic sentence.
       Contains the subject, verbs(predicate) and object.'''
    def __init__(self, subj, verb, obj):
        self.subj = subj[1]
        self.verb = verb[1]
        self.obj = obj[1]


class ParserError(Exception):
    '''Intercepts scraping errors.'''
    pass


def peek(word_list):
    # Returns the element type of the first tuple of the list
    # otherwise the value None.
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def mtch(word_list, expecting):
    # Compares the word type of the first tuple of the list.
    # When matching returns this tuple otherwise the value None.
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    # ...
    while peek(word_list) == word_type:
        mtch(word_list, word_type)


def parse_verb(word_list):
    # Returns the predicate(verb).
    skip(word_list, 'stop')    # Removes tuples with words like stop-word from the list.

    match peek(word_list):
        case 'verb':
            return mtch(word_list, 'verb')
        case _:
            raise ParserError("Expected a verb next.")


def parse_object(word_list):
    # Returns the direction.
    skip(word_list, 'stop')

    match peek(word_list):
        case 'noun':
            return mtch(word_list, 'noun')
        case 'direction':
            return mtch(word_list, 'direction')
        case _:
            raise ParserError("Expected a noun or direction next.")


def parse_subject(word_list):
    # Returns the object.
    skip(word_list, 'stop')

    match peek(word_list):
        case 'noun':
            return mtch(word_list, 'noun')
        case 'verb':
            return ('noun', 'player')
        case _:
            raise ParserError("Expected a verb next.")


def parse_sentence(word_list):
    # The main method.
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
