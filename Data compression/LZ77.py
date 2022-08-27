def zalgo(argv_str, end):
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
        if i >= end:
            break
        
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

            # case 2b: z[k] >= remaining
            elif z[k] > remaining:
                z[i] = remaining

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

class lz77:
    def __init__(self, data, window, buffer):
        self.data = data
        self.window = window
        self.buffer = buffer

    def compression(self):
        i = 0
        encoded_list = []
        while i < len(self.data):
            encoding = self.encode(i)
            encoded_list.append(encoding)
            i += encoding[1] + 1
        return encoded_list

    def encode(self, index):
        # Use z-algorithm to find longest prefix that matches.
        buffer = self.data[index : index + self.buffer]
        dicti = self.data[max(0, index - self.window) : index]

        text = ( buffer + " " + 
        dicti+ buffer )
        offset = 0
        match_length = 0
        end = len(buffer) + 1 + len(dicti)
        z = zalgo(text, end)
        
        if z[self.buffer + 1] is not None:
            tmp = z[self.buffer + 1 :]
            alist = max([0 if i is None else i for i in tmp])
            offset = end - tmp.index(alist) - self.buffer - 1
            match_length = alist
            next_char = self.data[index + alist]

        else:
            match_length = 0
            offset = 0
           
            next_char = self.data[index]  
        
        return offset, match_length, next_char