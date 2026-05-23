class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hsmp_row = {}
        hsmp_col = {}
        hsmp_cajas = {}

        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                if num != '.':
                    coord_caja = (i//3, j//3)
                    if j not in hsmp_col:
                        nums = set()
                        nums.add(num)
                        hsmp_col[j] = nums
                    else:
                        set_nums = hsmp_col[j]
                        if num not in set_nums:
                            set_nums.add(num)
                            hsmp_col[j] = set_nums
                        else:
                            return False
                    
                    if coord_caja not in hsmp_cajas:
                        nums = set()
                        nums.add(num)
                        hsmp_cajas[coord_caja] = nums
                    else:
                        set_nums = hsmp_cajas[coord_caja]
                        if num not in set_nums:
                            set_nums.add(num)
                            hsmp_cajas[coord_caja] = set_nums
                        else:
                            return False
            
                    if i not in hsmp_row:
                        nums = set()
                        nums.add(num)
                        hsmp_row[i] = nums
                    else:
                        set_nums = hsmp_row[i]
                        if num not in set_nums:
                            set_nums.add(num)
                            hsmp_row[i] = set_nums
                        else:
                            return False
        return True
                    


