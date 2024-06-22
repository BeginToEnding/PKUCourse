def compute_lps(pattern):
    lps = [0] * len(pattern)
    i = 1
    while i < len(pattern):
        j = lps[i - 1]
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            lps[i] = j + 1
        i += 1
    return lps


def kmp(text, pattern):
    if not text or not pattern or len(text) < len(pattern):
        return -1
    lps = compute_lps(pattern)
    i = 0
    j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - j
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


text = 'ABABDABACDABABCABAB'
pattern = 'ABABCABAB'
result = kmp(text, pattern)
if result != -1:
    print("Pattern found at index:", result)
else:
    print("Pattern not found in text.")