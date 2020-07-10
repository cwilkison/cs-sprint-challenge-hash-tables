# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    result = []


    for path in files:
        # splits up file paths after /
        item = path.split('/')[-1]

        # check cache and create new if not found
        if item not in cache:
            cache[item] = [path]
        # check cache, if found append
        else:
            cache[item].append(path)

    # loop to see if queries are in cache
    for q in queries:
        if q in cache:
            result += cache[q]
    
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
