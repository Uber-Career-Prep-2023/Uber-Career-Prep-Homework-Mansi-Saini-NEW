# Question: ReverseWords
# Technique Used: Stack
# Time Complexity: O(n) - have to traverse the entire string
# Space Complexity: O(n) - storing on a stack
# Time Spent: 25 min

"""
    Goal: Given a string, return the string with the order of the space-separated words reversed
    Parameters: a string
    Output: reversed sentence
"""
def ReverseWords(in_str):
    # edge case check: empty string
    if len(in_str) == 0:
        return

    # edge case check: one letter string
    if len(in_str) == 1:
        return in_str
    
    split_sentence = in_str.split()    # split string 
    word_stack = [] # create stack
    
    # add words to stack
    for i in split_sentence:
        word_stack.append(i)
    
    reverse_string = []
    while word_stack: # go through stack until empty
        reverse_string.append(word_stack.pop()) # add words from stack onto output list
    return " ".join(reverse_string) # output string by joining the words back together

# Test Cases
if __name__ == "__main__":
    print(ReverseWords("Uber Career Prep")) 
    print(ReverseWords("Emma lives in Brooklyn, New York.")) 
    print(ReverseWords("city the to welcome Emma,")) 
    print(ReverseWords("alligator later you see")) 
    print(ReverseWords("in a while crocodile"))
    print(ReverseWords("oh uh")) 