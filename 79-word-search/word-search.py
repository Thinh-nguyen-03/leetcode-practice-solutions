class Solution:
    
    def exist(self, board, word):
        
        def backtrack(row, col, index):
            
            # Check if the entire word is found
            if index == len(word):
                return True
            
            # Check boundaries and if the current cell matches the word character
            if (row < 0 or row >= len(board) or
                col < 0 or col >= len(board[0]) or
                board[row][col] != word[index]):
                return False
            
            # Mark the cell as visited
            temp = board[row][col]
            board[row][col] = '#'
            
            # Explore all possible directions
            found = (backtrack(row + 1, col, index + 1) or
                     backtrack(row - 1, col, index + 1) or
                     backtrack(row, col + 1, index + 1) or
                     backtrack(row, col - 1, index + 1))
            
            # Unmark the cell
            board[row][col] = temp
            
            return found
        
        # Iterate over each cell in the board
        for row in range(len(board)):
            for col in range(len(board[0])):
                
                # Start backtracking if the first character matches
                if board[row][col] == word[0] and backtrack(row, col, 0):
                    return True
        
        return False