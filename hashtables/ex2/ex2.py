#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    route = [None] * length


    for ticket in tickets:
        # starts with first destination at "NONE and adds to first element"
        if ticket.source == "NONE":
            route[0] = ticket.destination
        # cache source and destination as key, value
        else:
            cache[ticket.source] = ticket.destination
    # start to check rest of tickets
    if length > 1:
        # for loop to construct route using i location and checking  hash for the i-1 location
        # use tickets destination to add to route
        for i in range(1, length):
            route[i] = cache[route[i-1]]

    return route
