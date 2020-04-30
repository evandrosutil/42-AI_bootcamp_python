import time


def shuffle_list(list_obj):
    '''
    Essa função embaralhar uma lista passada usando time.process_time para
    aleatoriezar o processo.

    Args:
        list_obj (list): The list that will be shuffled.

    Returns:
        list: The shuffled list.
    '''

    list_len = len(list_obj) - 1
    while list_len >= 1:
        list_len = list_len - 1
        idx = int(str(time.process_time()).split('.')[-1][-1])
        if list_len == idx:
            continue
        if idx > len(list_obj) - 1:
            idx = int(idx / 2)
        list_obj[idx], list_obj[list_len] = list_obj[list_len], list_obj[idx]


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
        shuffle_list(text)
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
