'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if word == "" : return 0
    if word[-1].isnumeric() == False:  word = word + '0'
    if word[0] == word[-1] or word[1] == word[-1]: return int(word[-1])
    if word[0] == "t" and word[1] == "h": word = word[:-1] + str(int(word[-1]) + 1)
    #print(word)
    return count_th(word[1:])
