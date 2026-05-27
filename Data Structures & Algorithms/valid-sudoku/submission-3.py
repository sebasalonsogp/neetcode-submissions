class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = len(board)
        cols = len(board[0])
        
        # Check all rows
        for row in range(rows):
            myRow = set()
            for col in range(cols):
                val=board[row][col]
                if val == '.':
                    continue

                if val in myRow:
                    print('Returned False in row check')
                    return False
                myRow.add(val)

        # check cols
        for col in range(cols):
            myCol = set()
            for row in range(rows):
                val = board[row][col]
                if val == '.':
                    continue
                if val in myCol:
                    print('Returned False in column check')
                    return False
                myCol.add(val)

        # 3 x 3 grid --> hashmap of sets
        myGrids = collections.defaultdict(set)
        for row in range(rows):
            for col in range(len(board[row])):
                val = board[row][col]
                if val == '.':
                    continue
                if val in myGrids[(row//3,col//3)]:
                    print('Returned False in grid check')
                    return False
                myGrids[row//3,col//3].add(val)

        return True

