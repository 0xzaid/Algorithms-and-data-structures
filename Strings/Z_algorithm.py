"""
Implementation of Gusfield's Z-algorithm
"""
def zalgo(argv_str):
    """
    Function that uses the Z-Algorithm to produce a z-array
    """
    # creating z array
    z = [None]*len(argv_str)
    z[0] = len(argv_str)
    # zbox
    l, r = 0,0
    # pointer
    i = 1
    # loop through string
    while i < len(argv_str):
        
        # all the var
        k = i-l
        
        remaining = r-i+1
        """
        cases
        """
        # case 1: Outside the box
        if i > r:
            l, r = i, i
            while r < len(argv_str) and argv_str[r-l] == argv_str[r]:
                r = r+1
            z[i] = r - l
            r = r-1
        
        # case 2a, 2b, 2c : inside box
        else:
            
            # case 2a: z[k] < remaining
            if z[k] < remaining:
                z[i] = z[k]
                
            # case 2b: z[k] > remaining
            elif z[k] > remaining:
                z[i] = remaining
            
            # case 2c: z[k] = remaining
            elif z[k] == remaining:
                l = i
                # x = remaining
                while r < len(argv_str) and argv_str[r-l] == argv_str[r]:
                    r = r+1
                z[i] = r - l
                r = r-1
                
        # increment
        i += 1
    return z

if __name__ == "__main__":
    text1 = 'abcdabcdabcdabcdabcdabcd'
    text11 = zalgo(text1)
 
    
    print(text11)

    