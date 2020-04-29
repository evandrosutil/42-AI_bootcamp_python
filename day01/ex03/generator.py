from random import shuffle


def generator(text, sep=" ", option=None):
    '''
    A simple generator.

    Args:
        text (str): The text to be splitted.
        sep (:obj:`str`, optional): The separator used to break the text.
        option (:obj:`str, optional): The order in which the words are showed.
            The options are `suffle`, `unique` and `ordered`.

    Yields:
        str: the next part of the text.
    '''
    if (
            not isinstance(text, str)
            or (option and option not in ['shuffle', 'ordered', 'unique'])
    ):
        print('ERROR')
        return None
    text = text.split(sep)
    if option == 'shuffle':
        shuffle(text)
    elif option == 'ordered':
        text.sort()
    elif option == 'unique':
        text = set(text)

    for word in text:
        yield word


if __name__ == '__main__':
    text = 'Le Lorem Ipsum est simplement du faux texte.'
    print('error:')
    for word in generator(text, option='error'):
        print(word)
    print('\nordered:')
    for word in generator(text, sep=" ", option='ordered'):
        print(word)
    print('\nunique:')
    for word in generator(text, option='unique'):
        print(word)
    print('\nshuffle:')
    for word in generator(text, option='shuffle'):
        print(word)
