def same_structure_as(original, other):
    if len(original) != len(other):
        return False
    for n in range(0, len(original)):
        if isinstance(original[n], list) and isinstance(other[n], list):
            res = same_structure_as(original[n], other[n])
            if not res:
                return False
        elif isinstance(original[n], other[n]):
            return False
    return isinstance(original, other)
