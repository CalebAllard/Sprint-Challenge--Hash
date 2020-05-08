#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

cache = {}
def reconstruct_trip(tickets, length):
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    route = []
    route.append(cache["NONE"])
    current_ticket = cache["NONE"]
    while len(route) < length:
        if current_ticket in cache:
            route.append(cache[current_ticket])
            current_ticket = cache[current_ticket]
    return route

        

   
    """
    YOUR CODE HERE
    """

    return route
