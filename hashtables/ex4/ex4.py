def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []

    for integer in a:
        # check all numbers not 0
        if integer != 0:
            # add integer to cache
            cache[integer] = True
            # if integer has opposite integer in cache....
            if -integer in cache:
                # append absolute integer to results array
                result.append(abs(integer))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
