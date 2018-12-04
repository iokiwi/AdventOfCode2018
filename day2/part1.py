def read_input():
    i = input()
    values = []
    while(i):
        try: 
            values.append(i)
            i = input()
        except EOFError:
            break
    return values

def count_chars(identifier):
    char_count = dict()
    for char in identifier:
        if char in char_count.keys():
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def checksum(id_list):
    """
    >>> checksum(['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab'])
    12
    """

    two_count = 0
    three_count = 0

    for identifier in id_list:
        char_count = count_chars(identifier)

        if 2 in char_count.values():
            two_count += 1
        if 3 in char_count.values():
            three_count += 1

    return two_count * three_count

def main(): 
    values = read_input()
    answer = checksum(values)
    print(answer)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()