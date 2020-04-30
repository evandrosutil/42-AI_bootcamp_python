class Evaluator():

    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        words_len = [len(c) for c in words]
        res = zip(coefs, words_len)
        result = [a * b for a, b in res]

        return sum(result)

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        words_len = [len(c) for c in words]
        res = 0
        for i, b in enumerate(words_len):
            res += (b * coefs[i])

        return res
