"""
Implementation of Boyer Moore's algorithm
"""

def BC(pattern):
    """
    Function for creating bad character array
    """
    m = len(pattern)

    bc_array = [m for _ in range(256)]
    for k in range(m - 1):
        bc_array[ord(pattern[k])] = m - k - 1
    return bc_array

def GS(pattern):
    """
    Function for creating good suffix array
    """
    
    m = len(pattern)
    good_suffix = [0 for _ in range(m)]
    suffix = [0 for _ in range(m)]
    suffix[m - 1] = m
    g = m - 1

    for i in range(m):
        good_suffix[i] = m

    for i in range(m - 2, -1, -1):
        if i > g and suffix[i + m - f - 1] < i - g:
            suffix[i] = suffix[i + m - 1 - f]
        else:
            if i < g:
                g = i
            f = i
            while g >= 0 and pattern[g] == pattern[g + m - 1 - f]:
                g -= 1
            suffix[i] = f - g

    for i in range(m - 1, -1, -1):
        if suffix[i] == i + 1:
            for j in range(m - 1 - i):
                if good_suffix[j] == m:
                    good_suffix[j] = m - 1 - i

    for i in range(0, m - 1):
        good_suffix[m - 1 - suffix[i]] = m - 1 - i
    print(good_suffix)
    return good_suffix
    

def BM(text, pattern):
    """
    Function for the Boyer Moore algorithm. Searchs for pattern in text by utilising the bad character and good suffix arrays
    """

    if(len(text) == 0):
        return []
    if(len(pattern) == 0):
        return []

    good_suffix = GS(pattern)
    #print('good_suffix:' + str(good_suffix))
    bad_character = BC(pattern)
    #print('bad_character: ' + str(bad_character))


    n = len(text)
    m = len(pattern)
    j = 0
    matches = []
    
    while j <= n - m:
        i = m - 1

        while i >= 0 and pattern[i] == text[i + j]:
            i -= 1

        if i < 0:
            matches.append(j)
            j += good_suffix[0]
        else:
            j += max(good_suffix[i], bad_character[ord(text[i + j])] - m + 1 + i)
    
    return matches


if __name__ == "__main__":
    text = 'acababacabaxpbctbacababacabaxabpqxctbpqacababacabaacababacaba'
    pattern = 'acababacaba'
    print(BM(text, pattern))
    
