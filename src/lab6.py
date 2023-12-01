def build_pi_array(pattern):
    pattern_length = len(pattern)
    pi = [0] * pattern_length
    j = 0

    for i in range(1, pattern_length):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]

        if pattern[i] == pattern[j]:
            j += 1

        pi[i] = j

    return pi


def match(input_pos, pattern_pos, pi, haystack, needle):
    while (
            pattern_pos < len(needle)
            and input_pos < len(haystack)
            and needle[pattern_pos] == haystack[input_pos]
    ):
        pattern_pos += 1
        input_pos += 1

    if pattern_pos == len(needle):
        return input_pos - pattern_pos
    elif pattern_pos != 0:
        pattern_pos = pi[pattern_pos - 1]
    else:
        input_pos += 1

    return -1


def knuth_morris_pratt(haystack, needle):
    if not haystack or not needle:
        return []

    pi = build_pi_array(needle)
    indexes = []
    input_pos, pattern_pos = 0, 0

    while input_pos < len(haystack):
        match_pos = match(input_pos, pattern_pos, pi, haystack, needle)
        if match_pos != -1:
            indexes.append(match_pos)
            input_pos = match_pos + 1
            pattern_pos = 0
        elif pattern_pos != 0:
            pattern_pos = pi[pattern_pos - 1]
        else:
            input_pos += 1

    return indexes
