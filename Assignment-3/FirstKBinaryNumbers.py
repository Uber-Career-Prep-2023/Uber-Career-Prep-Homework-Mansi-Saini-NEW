# Question: FirstKBinaryNumbers
# Technique Used: Built-in binary conversion library
# Time Complexity: O(k * log k) - dependent on input number
# Space Complexity: O(k) - dependent on input
# Time Spent: 11 minutes

"""
    Goal: Given a number, k, return an array of the first k binary numbers, represented as strings.
    Parameters:  k - number of binary numbers to generate
    Output: k binary numbers
"""
def FirstKBinaryNumbers(k):
    bin_nums = []

    # continue generating until k
    for i in range(k):
        # built-in binary conversion python function and add number to output array
        bin_nums.append(bin(i)[2:]) # splice to remove uncessary string info
    return bin_nums # return output array

# Test Cases
if __name__ == "__main__":
    # print(FirstKBinaryNumbers(5))
    assert FirstKBinaryNumbers(5) == ['0', '1', '10', '11', '100']
    
    # print(FirstKBinaryNumbers(10))
    assert FirstKBinaryNumbers(10) == ['0', '1', '10', '11', '100', '101', '110', '111', '1000', '1001']