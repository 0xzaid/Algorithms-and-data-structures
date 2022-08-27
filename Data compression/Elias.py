from bitarray import bitarray

def elias_encode(number_to_encode):
    """
    function to find elias code for given number
    """
    list_of_length = []
    number_to_encode = number_to_encode
    n = format(number_to_encode, 'b')
    len_rule = len(n) - 1

    while len_rule > 1:
        encode = format(len_rule,'b')
        encoded_list = list(encode)
        encoded_list[0] = "0"
        
        encode = "".join(encoded_list)
        list_of_length.append(encode)
        len_rule = len(encode) - 1

    if number_to_encode <= 1:
        pass
    else:
        list_of_length.append("0")
        list_of_length.reverse()

    result = "".join(list_of_length) + n
    #result = bitarray(result)
    return result


def elias_decode(binary_data):
    read_len = int("1",2)
    component = []
    pos = 0
    check = True
    while check:
        component = binary_data[pos:pos + read_len]
        if component[0] == "1":
            N = int(component, 2)
            check = False
        else:
            # if msb of component is 0, then flip
            temp = list(component)
            # flip
            temp[0] = "1"
            component = "".join(temp)
            dec_component = int(component,2)
            pos = pos + read_len
            read_len = dec_component + 1
    return N

if __name__ == "__main__":
    n = 561
    encoded = elias_encode(n)
    print(encoded)
    decoded = elias_decode(encoded)
    print(decoded)