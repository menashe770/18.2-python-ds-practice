def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """

    dict1 = {}
    dict2 = {}

    for i in str(num1):
        dict1[i] = dict1.get('i', 0) + 1

    for j in str(num2):
        dict2[j] = dict2.get('j', 0) + 1

    return dict1 == dict2
