

def finder(files, queries):
    cache = {}
    result = []
    for i in range(0, len(files)):
        arr = files[i].split('/')
        if arr[len(arr) - 1] not in cache:
            cache[arr[len(arr) - 1]] = []
            cache[arr[len(arr) - 1]].append(files[i])
        elif arr[len(arr) - 1] in cache:
            cache[arr[len(arr) - 1]].append(files[i])
                
            
        else:
            continue
    for i in queries:
        if i in cache:
            for k in cache[i]:
                result.append(k)
    """
    YOUR CODE HERE
    """
    print(result)
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
