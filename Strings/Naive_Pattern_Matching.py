"""
Naive pattern matching algorithn       
"""

def naive_pattern_match(text, pattern):
    n, m, result = len(text), len(pattern), []
    for i in range(n-m+1):
        j = 0
        while j < m:
            if text[i+j] != pattern[j]:
                break
            j += 1
        if(j==m):
            result.append(i)
    return result
        
if __name__ == '__main__':
    text = 'abracadabra'
    pattern = 'ab'
    print(text)
    print("The patterns exist at indices: " + str(naive_pattern_match(text, pattern)))
            