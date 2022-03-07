"""
Problem Statement
----------------
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.  Note that the same word in the dictionary may be reused multiple times in the segmentation.


Input
-----
a word and a word dictionary (list)

Output
-------
boolean
"""


def word_break(s, word_dict):
    word_dict = set(word_dict)
    cache = {}

    def can_break(word):
        if word in cache:
            return cache[word]
        if word == "":
            return True

        for dict_word in word_dict:
            if word.find(dict_word) == 0:
                remaining_word = word[len(dict_word):]
                if can_break(remaining_word):
                    cache[remaining_word] = True
                    return True

        cache[word] = False
        return False

    return can_break(s)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
