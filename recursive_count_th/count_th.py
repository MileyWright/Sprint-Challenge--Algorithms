'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    if len(word) < 2: # Base case, can't be 'th' if it's less than 2 characters.
        return 0
    
    if word[:2] == 'th':  # looks for 'th' in indexes
        return count_th(word[1:]) + 1  # Move indexes 
    else:
        return count_th(word[1:]) # remove first index
    
    pass
