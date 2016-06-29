def to_romans(number):
    roman = ''
    mapping = [(40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    for (arabic, roman_mapping) in mapping:
        occurences = number // arabic
        roman += roman_mapping * occurences
        number -= arabic * occurences
    return roman
