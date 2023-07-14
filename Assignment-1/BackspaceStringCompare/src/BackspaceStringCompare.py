# Question: BackspaceStringCompare
# Technique Used: Simultaneous Iteration Two-Pointer
# Time Complexity: O(n) - Traverse two 1-D arrays at the same time
# Space Complexity: O(n) - Two 1-D arrays created (2n)
# Time Spent: 42 min - Finished!

# Directions: Given two strings representing series of keystrokes, 
# determine whether the resulting text is the same. Backspaces 
# are represented by the '#' character so "x#" results in the empty string ("").

# Thought Process
    # create two output lists
    # traverse through both strings at the same time

    # first string
    # if current letter in first string is '#'
        # make sure list isn't empty
            # delete element from end of output1 list
    
    # second string
    # if current letter in second string is '#'
        # make sure list isn't empty
            # delete element from end of output2 list

    # merge lists to strings and return if they are equal or not


def BackspaceStringCompare(string1, string2):
    # create output lists
    first = []
    second = []

    # first string iteration
    for i in string1:
        if i == '#': # deletion check
            if len(first) > 0: # make sure list isn't empty
                first.pop() # backspace in first string list
        else:
            first.append(i) # no character to delete so we add to output list
    
    # second string iteration
    for x in string2:
        if x =='#': # deletion check
            if len(second) > 0: # make sure list isn't empty
                second.pop() # backspace in second string list
        else:
            second.append(x) # no character to delete so we add to output second list
    
    # join output lists back into strings
    string1 = ''.join(first)
    string2 = ''.join(second)

    return string1 == string2 # see if modified strings are the same

BackspaceStringCompare("", "")
BackspaceStringCompare("abcde", "abcde")
BackspaceStringCompare("Uber Career Prep", "u#Uber Careee#r Prep")
BackspaceStringCompare("abcdef###xyz", "abcw#xyz")
BackspaceStringCompare("abcdef###xyz", "abcdefxyz###")


