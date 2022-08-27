"""
Implementation of Knuth-Moris-Pratt algorithm
"""

from Z_algorithm import zalgo

def longest_proper_suffix(pat):
    z = zalgo(pat)
    print("Z array: " + str(z))
    m = len(pat)
    
    lps_list = m*[0]
    for i in range(m):
        lps_list[i] = 0
        for j in range(m-1,0,-1):
            i = j+z[j]-1
            lps_list[i] = z[j]
    return lps_list  


def KMP(text, pat):
    lps = longest_proper_suffix(pat)
    n = len(text)
    m = len(pat)
    result = []
    j = 0
    i = 0
    
    while i < n:
        if pat[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            result.append(i-j)
            j = lps[j-1]
        elif i < n and pat[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return result
    

if __name__ == "__main__":
    text = 'ABCDMXYT ABABCDABD ABCDABD'
    pat = 'ABCDABD'
    expected_lps = [0, 1, 0, 0, 0, 0, 0, 1, 3, 0, 1, 0]
    lps_list = longest_proper_suffix(pat)
    print("Expected: "+ str(expected_lps))
    print("Actual: " + str(lps_list))
    
    print(KMP(text, pat))
    
    #print(z)
    #print(KMP(text, pat, z))