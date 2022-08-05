def first_non_repeating_character(string):
    lower = string.lower()
    for i, s in enumerate(lower):
        if lower.count(s) == 1:
            return string[i]
    return ''
