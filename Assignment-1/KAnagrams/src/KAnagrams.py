# Question: KAanagrams
# Technique Used: Sort then Solve (convert to set -> difference of the two)
# Time Complexity: O(n)
# Space Complexity: O(n)
# Time Spent: 22 min - Finished!

# Directions: Write a function that addresses the
# following problem and define test cases
# to check the function itself

# Two strings are considered to be “k-anagrams”
# if they can be made into anagrams by changing
# at most k characters in one of the strings.
# Given two strings and an integer k, determine
# if they are k-anagrams.

# Thought Process
    # FASTER SOLUTION
    # edge case check: strings are not the same length; cannot change characters that don't exist
    # convert both strings to sets - O(n)
    # find the difference between the two sets - O(n*m)
        # if the length of the difference of both strings are less than or equal to k,
            # then we know it is a k-anagram
        # otherwise, 
            # we know it is NOT a k-anagram


    # SORT THEN SOLVE SOLUTION (SIMULTANEOUS TWO POINTER ITERATION)
    # create counter
    # sort both strings - o(nlogn)
        # e.g. aelpp, acehp
        # two pointer simulataneous iteration
            # if current letter is the same in both
                # skip letter
            # else if different letters
                # increase counter
            # if the counter is greater than k, (takes more swaps than allowed)
                # we know its not k-anagrams and can return false

    # if the counter is less than or equal to k, 
        # then we know its k-anagrams and can return true



def KAnagrams(string1, string2, k):
    # edge case check: different size strings
    if (len(string1) != len(string2)):
        return False

    # difference between two strings - letters not in both strings
    diff = set(string2).difference(string1) 
    other = set(string1).difference(string2)

    if (len(diff) <= k and len(other) <= k): # can change at most k characters
        return True
    else: # cannot change at most k characters or invalid response
        return False 


# Tests
KAnagrams("", "", 1)
KAnagrams("apple", "apple", 3)
KAnagrams("apple", "peach", 1)
KAnagrams("apple", "peach", 2)
KAnagrams("cat", "dog", 3)
KAnagrams("debit curd", "bad credit", 1)
KAnagrams("baseball", "basketball", 2)

