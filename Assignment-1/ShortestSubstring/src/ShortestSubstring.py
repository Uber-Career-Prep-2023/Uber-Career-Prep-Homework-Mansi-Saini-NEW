# Question: ShortestSubstring
# Technique Used: Growing/Shrinking Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1) - not creating any other structures to store elements; only going through characters in string
# Time Spent: 40 min - DNF
    # realized I cannot say if one string contains another 
    # since it compares the entire string (instead of each character)
    # might need to create a dictionary to take care of the occurrences


# Directions: Write a function that addresses the
# following problem and define test cases
# to check the function itself

# Thought Process

    # might need to create a dictionary to store the second string (prevent more loops) - note for future

    # create left pointer
    # create right pointer
    # create smallest subarray length to store later
    # iterate through string1 until left pointer reaches end
        # if right edge has not reached the end (meaning it cannot expand more)
        # and window does not contain string2
        # expand to the right
        # increase window size by incrementing right edge
    # otherwise, if the window does contain string2,
        # shrink window size from the left
    # if current window size is smaller than smallest subarray length,
        # update smallest subarray length with current subarray length
    # otherwise, the window doesn't contain string2 and we have reached the end of string1
        # end loop; break;

    # return the smallest subarray length that contains string2

def ShortestSubstring(string1, string2):
    left = 0  # left pointer
    right = 0  # right pointer end
    small_sub_len = 0  # init smallest subarray length to return later

    # iterate through string1 until left pointer reaches the end
    while (left < len(string1) - 1):
        # right edge has not reached the end and string2 is not in string1's window
        print(string1[left:right], string2)
        if ((right < len(string1) - 1) and (string2 not in string1[left:right])):
            right += 1  # expand window size to the right
        elif (string2 in string1[left:right]):
            # current subarray length is smaller than the minimum subarray length
            if (len(string1[left:right]) < small_sub_len):
                # update the newest minimum subarray length
                small_sub_len = len(string1[left:right])
            left += 1  # shrink window size by one
        else:
            # window doesn't ontain string2 and we have reached end of string1
            break
    print(small_sub_len)


ShortestSubstring("abracadabra", "abc")
ShortestSubstring("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx")
ShortestSubstring("dog", "god")
