from lib.count_words import *


"""
given an empty string
returns number of words
"""
def test_with_empty_string():
    actual = count_words("")
    expected = 0
    assert actual == expected

"""
given fewer than five words
returns number of words
"""
def test_with_words_fewer_than_five_words():
    actual = count_words("Hello world")
    expected = 2
    assert actual == expected


"""
given more than five words 
returns number of words
"""
def test_with_words_more_than_five_words():
    actual = count_words("Hello my name is John and I am happy") 
    expected = 9
    assert actual == expected

"""
given numbers seperated by spaces
returns the length
"""
def test_with_numbers_seperated_by_spaces():
    actual = count_words("1234 4343 3432") 
    expected = 3
    assert actual == expected