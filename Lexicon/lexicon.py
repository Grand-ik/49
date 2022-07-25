# Basic vocabulary.
word_types = {"direction": ["north", "south", "east", "west",
                            "down", "up", "left", "back"],
              "verb": ["go", "stop", "eat", "kill"],
              "stop": ["the", "in", "of", "from", "at", "it"],
              "noun": ["door", "bear", "princess", "cabinet"]}


def int_check(word):
    # Defines a string as a number or an error.
    if word:
        try:
            return [('number', int(word))]
        except ValueError:
            return [('error', word)]
    else:
        return None


def typer(word):
    # Defines a word by type or returns the value 'None'.
    if word:
        for key, value in word_types.items():
            if word in value:
                return [(key, word)]
    else:
        return None


def scan(sentence):
    # Defines the type of each word in the sentence.
    # Returns a list of tuples with a word type and a word or value None.
    array = []

    for word in sentence.lower().split():
        type_word = typer(word)
        if type_word:
            array += type_word
        else:
            array += int_check(word)

    return array
