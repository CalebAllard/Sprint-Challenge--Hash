
def has_negatives(a):
    cache = {}
    current = None
    result = []
    for i in a:
        if i < 0: 
            cache[i] = i
    for i in a:
        if i > 0:
            if -i in cache:
                result.append(i)
            else:
    
                continue
    # print(a)
    print(cache)
    print(result)
    return result            

    """
    YOUR CODE HERE
    """
    


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
