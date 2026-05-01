class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # First - Validate rows
        for i in range(len(board)):
            nums = [0] * len(board[0])
            for j in range(len(board[0])):
                value = board[i][j]
                if value != ".":
                    value_int = int(value)
                    nums[value_int-1] += 1
            if 2 in nums:
                return False
        # Second - Validate columns
        for j in range(len(board[0])):
            nums = [0] * len(board[0])
            for i in range(len(board)):
                value = board[i][j]
                if value != ".":
                    value_int = int(value)
                    nums[value_int-1] += 1
            if 2 in nums:
                return False
        # Third - Validate boxes
        for box_row in range(3):
            for box_col in range(3):
                nums = [0] * len(board[0])
                box = [
                    board[box_row * 3 + dr][box_col * 3 + dc]
                    for dr in range(3)
                    for dc in range(3)
                ]
                for value in box:
                    if value != ".":
                        value_int = int(value)
                        nums[value_int-1] += 1
                if 2 in nums:
                    return False
        return True