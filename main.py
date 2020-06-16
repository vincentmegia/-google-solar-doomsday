from math import sqrt

numbers = []


def main(input):
    """
    Main definition
    """
    # ans is 15324, 15129,169,25,1
    # x = 15324 - 15129 #195
    # x = 195 - 169 #26
    # x = 26 - 25 #1
    nearestsquare(input)

def nearestsquare(input):
    """
    Finding the nearest square
    """
    result = 0
    # for i in range(input - 1, 0, -1):
    i = input
    while input != 0:
        squareroot = sqrt(i)
        if squareroot.is_integer():
            numbers.append(i)
            result = input - i
            nearestsquare(result)
            break
        i = i - 1
    print "exit"
    print "exit"


if __name__ == "__main__":
    # main(15324)
    main(12)
