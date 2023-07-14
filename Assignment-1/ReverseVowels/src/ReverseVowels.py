# Question: MaxMeanSubArray
# Technique Used: Forward-Backward Pointer
# Time Complexity: O(n)
# Space Complexity: O(n)
# Time Spent: 36 minutes

# Directions: Write a function that addresses the
# following problem and define test cases
# to check the function itself

# Thought Process
    # one ptr at beginning
    # one ptr at end
    # traverse towards middle from both ends
    # continue towards middle until you hit a vowel
        # once both ptrs are vowels
        # swap them

def reverseVowels(input):
    # edge case check: empty input
    if (len(input) < 1):
        return

    front = 0 # left end
    back = len(input) - 1 # right end
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    input = list(input)
    for i in range(len(input)):
        if (front == back or front > back): # stop swapping
            break
        if (input[front] in vowels and input[back] in vowels): # hit 2 vowels case
            # swap the vowels
            tmp = input[front]
            input[front] = input[back]
            input[back] = tmp

            # update pointers
            front += 1
            back -= 1
        
        elif (input[front] not in vowels): # update front ptr
            front += 1
        elif(input[back] not in vowels): # update back ptr
            back -= 1
    
    input = ''.join(input)
    return input

reverseVowels("lkjhgfd") # no vowels
reverseVowels("") # empty string
reverseVowels("   ") # spaces only
reverseVowels("aeiouAEIOU") # only vowels
reverseVowels("Uber Career Prep")
reverseVowels("xyz")
reverseVowels("flamingo")
