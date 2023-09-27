def sort (names, scores, first: int):
    """Sorts a list of scores from smallest to largest and 
    sorts the list of names according to the order defined by 
    the sorted scores.

    Args:
        names: list of names
        scores: list of scores
        first (int): the list index at which the sort will begin
    """
    # initialize loop counter variables named i, j
    i = len(scores) - first - 1
    j = 0

    # initialize variable named big used to store index of biggest value
    big = 0

    # initialize variables named tempScore and tempName used to swap list values
    tempScore = 0
    tempName = ""
    
    while (i > 0):
        # set big equal to first
        big = first

        # set j equal to first + 1
        j = first + 1

        while (j <= first + i):
            # if value in scores[big] is less than value in scores[j], set big equal to j
            if (scores[big] < scores[j]):
                big = j

            # increment j
            j += 1
        
        # set tempScore to value in scores[first + i]
        # set tempName to value in names[first + i]
        tempScore = scores[first + i]
        tempName = names[first + i]

        # set data[first + i] to value in data[big]
        scores[first + i] = scores[big]
        names[first + i] = names[big]

        # set data[big] to value in temp
        scores[big] = tempScore
        names[big] = tempName

        # decrement i
        i -= 1