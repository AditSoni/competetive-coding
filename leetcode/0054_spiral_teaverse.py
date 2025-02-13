class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result =[]
        start_row,end_row = 0,len(matrix) - 1
        start_col,end_col = 0,len(matrix[0]) -1

        while start_row <= end_row and start_col <= end_col:
            print(f"{start_row=} {end_row=} {start_col=} {end_col=}")
            for col in range(start_col,end_col+1):
                print(f"{col=}")
                result.append(matrix[start_row][col])
            
            for row in range(start_row+1,end_row+1):
                print(f"{row=}")
                result.append(matrix[row][end_col])
            
            if start_row < end_row:
                for col in range(end_col-1,start_col-1,-1):
                    print(f"{col=}")
                    result.append(matrix[end_row][col])
            
            if start_col < end_col:
                for row in range(end_row-1,start_row,-1):
                    print(f"{row=}")
                    result.append(matrix[row][start_col])
            
            start_row+=1
            end_row-=1
            start_col+=1
            end_col-=1
        
        return result