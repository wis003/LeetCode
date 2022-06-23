class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        indices = [(1,1), (1,4), (1,7),
                   (4,1), (4,4), (4,7),
                   (7,1), (7,4), (7,7),]

        # check sub-boxes
        for i in indices:
            square = {}
            for j in range(-1, 2):
                for k in range(-1, 2):
                    curr = board[i[0] + j][i[1] + k]
                    if curr not in square:
                        square[curr] = 1
                    else:
                        square[curr] += 1
            for k,v in square.items():
                if v > 1 and k != '.':
                    return False
            
        # check rows and columns
        for i in range(9):
            horz = {}
            vert = {}
            for h in board[i][:]:
                if h not in horz:
                    horz[h] = 1
                else:
                    horz[h] += 1
            for v in [col[i] for col in board]:
                if v not in vert:
                    vert[v] = 1
                else:
                    vert[v] += 1
            for k,v in horz.items():
                if v > 1 and k != '.':
                    return False
            for k,v in vert.items():
                if v > 1 and k != '.':
                    return False
        return True
            