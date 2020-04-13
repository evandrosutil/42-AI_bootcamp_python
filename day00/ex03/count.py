import string


def text_analyzer(text=None):
    if not text:
        text = input("What is the text to analyse?\n")
    result = dict()
    for i in text:
        if i.isupper():
            result['upper'] = result.get('upper', 0) + 1
        if i.islower():
            result['lower'] = result.get('lower', 0) + 1
        if i == ' ':
            result['spaces'] = result.get('spaces', 0) + 1
        if i in string.punctuation:
            result['punctuation'] = result.get('punctuation', 0) + 1
            print(i)

    final_str = (
        f"The text contains {len(text)} characters:\n\n"
        f"- {result['upper']} upper letters\n\n"
        f"- {result['lower']} lower letters\n\n"
        f"- {result['punctuation']} punctuation marks\n\n"
        f"- {result['spaces']} spaces")

    print(final_str)
