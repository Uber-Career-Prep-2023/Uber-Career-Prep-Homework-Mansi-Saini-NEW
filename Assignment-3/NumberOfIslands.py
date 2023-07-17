# Question: NumberOfIslands
# Technique Used: Depth-first search
# Time Complexity: O(n)
# Space Complexity: O(n)
# Time Spent: 38 min
# Thought Process: Go through the board, for every possible island (a 1), perform a depth first search making sure that the adjacent regions are valid for the conditions of an island


"""
    Goal: Given a binary matrix in which 1s represent land and 0s represent water. Return the number of islands (contiguous 1s surrounded by 0s or the edge of the matrix).
    Parameters: a board
    Output: number of islands
"""
def NumberOfIslands(board):
    # edge case check: board does not exist
    if not board:
        return 0  # no islands

    num_islands = 0  # count number of islands

    # traverse the board
    for i in range(len(board)):
        for x in range(len(board[0])):
            # see if we reached a possible island
            if board[i][x] == 1:
                # if so, perform depth-first search
                dfs(board, i, x)
                num_islands += 1  # increment island count
    return num_islands  # output island count

"""
    Goal: perform a depth-first search in the board to ensure there exists an island
    Parameters: board, row/column iterators
"""
def dfs(board, i, x):
    # edge case check: invalid row/column or not a possible island
    if i < 0 or x < 0 or i >= len(board) or x >= len(board[0]) or board[i][x] != 1:
        return

    board[i][x] = 'v' # square has been visited

    # go through adjacent squares for each region in the matrix
    dfs(board, i + 1, x)
    dfs(board, i - 1, x)
    dfs(board, i, x + 1)
    dfs(board, i, x - 1)


# Test Cases
if __name__ == "__main__":
    test_board = [[1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0]]

    # print(NumberOfIslands(test_board))
    assert NumberOfIslands(test_board) == 3


    second_test_board = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [
        1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]

    # print(NumberOfIslands(second_test_board))    
    assert NumberOfIslands(second_test_board) == 1


    third_test_board = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [
        0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]

    # print(NumberOfIslands(third_test_board))
    assert NumberOfIslands(third_test_board) == 3


    fourth_test_board = [[1, 0, 0], [0, 0, 0]]

    # print(NumberOfIslands(fourth_test_board))
    assert NumberOfIslands(fourth_test_board) == 1

