'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Set variable containin letter to check for
    t = "t"
    h = "h"
    
    # Check if word is empty

    # If empty
    if word == "":
        # return 0
        return 0

    # If the lenght of the string is greater or equal than two
    if len(word) >= 2:
        
        # if word[0] is t AND word[1] is h:
        if word[0] == t and word[1] == h:
            # return 1 + count_th(word[2:])
            return 1 + count_th(word[2:])
        # else
        else:
            # return count_th(word[1:])
            return count_th(word[1:])
    # else:
    else:
        # return 0
        return 0


# Testing 
word = "thhtthht"
th_count = count_th(word)
print(f"\nThe count of {word} is {th_count}")
