from studentscores import *

def main():
    # set up the lists and first
    names = ["Emma", "Brian", "Evelyn", "Frank", "Alex", "Felicia", "Carl"]
    scores = [99, 85, 64, 78, 95, 50, 88]
    first = 0

    # display original unsorted lists
    print("ORIGINAL LISTS")
    print("Names", "Scores")
    i = 0
    while (i < len(names)):
        print(names[i], scores[i])
        i += 1
    
    # call the sort function
    sort(names, scores, first)

    print()

    # display the sorted lists
    print("SORTED LISTS")
    print("Names", "Scores")
    i = 0
    while (i < len(names)):
        print(names[i], scores[i])
        i += 1

if __name__ == "__main__":
    main()