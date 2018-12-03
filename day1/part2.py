def read_input():
    i = input()
    values = []
    while(i):
        try: 
            values.append(int(i))
            i = input()
        except EOFError:
            break
    return values


def iterate_values(values, frequency_history=None, start_frequency=0):
    """ Return the first recurring frequency
    >>> iterate_values([1, -1])
    0
    >>> iterate_values([3, 3, 4, -2, -4])
    10
    >>> iterate_values([-6, 3, 8, 5, -6])
    5
    >>> iterate_values([7,7,-2,-7,-4])
    14
    """

    frequency = start_frequency

    if frequency_history is None:
        frequency_history = set()

    #print("{:<10}{:<10}{:<10}{}".format("f", "v", "f+v", "history"))

    for value in values:
        frequency_history.add(frequency)
        #print("{:<10}{:<10}{:<10}{}".format(frequency, value, frequency + value, frequency_history))
        frequency += value
        if frequency in frequency_history:
            return frequency
    return iterate_values(values, frequency_history, frequency)


def main():	
    values = read_input()
    answer = iterate_values(values)
    print(answer)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()