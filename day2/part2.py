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


def compare_ids(id_1, id_2):
    """ Compare two ids and return differences
        @param id_1 the first id
        @param id_1 the second id
        @return a list of differnces betweens id_1 and id_2 formatted as a tuple of the index of the difference, the letter in id_1 and the letter in id_2
    """
    differences = []
    for i in range(len(id_1)):
        if id_1[i] != id_2[i]:
            differences.append((i, id_1[i], id_2[i]))
    return differences


def find_correct_box_ids(id_list):
    """ Find the close pair of id's with only 1 differences
        @param a list of ids
        @return a tuple of 2 ids which only have one letter different
    """
    for i in id_list:
        for j in id_list:
            compare_result = compare_ids(i, j)
            if len(compare_result) == 1:
                return (i, j)


def common_letters(id_list):
    """
    >>> common_letters(['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz'])
    'fgij'
    """
    pair = find_correct_box_ids(id_list)
    pair_difference = compare_ids(pair[0], pair[1])[0]
    char_list = list(pair[1])
    char_list.pop(pair_difference[0])
    return "".join(char_list)


def main(): 
    values = read_input()
    answer = common_letters(values)
    print(answer)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()