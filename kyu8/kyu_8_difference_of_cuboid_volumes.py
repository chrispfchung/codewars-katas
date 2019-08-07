def find_difference(a, b):
    # take two lists of integers ( a and b )
    # find difference of the cuboids volumes
    # size does not matter
    # each list consists of 3 positive integers > 0

    # PLAN
    # Multiply elements in each list
    # absolute(subtract)
    import numpy
    return abs( (numpy.prod(a)-numpy.prod(b)) )
