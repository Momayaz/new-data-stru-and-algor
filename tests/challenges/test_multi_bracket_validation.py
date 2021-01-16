from data_structures_and_algorithms.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket


def test_multi_bracket_validation_without_text():
    actual = multi_bracket('{}')
    expected = True
    assert actual == expected

def test_multi_bracket_validation_with_missing_curly_braces():
    actual = multi_bracket('{({})')
    expected = False
    assert actual == expected
    
def test_multi_bracket_validation_without_text_two():
    actual = multi_bracket('{({})}')
    expected = True
    assert actual == expected

def test_multi_bracket_validation_with_word():
    actual = multi_bracket('{()[[any text]]}')
    expected = True
    assert actual == expected

def test_multi_bracket_validation_with_extra_curly_braces():
    actual = multi_bracket('{({})}}')
    expected = False
    assert actual == expected