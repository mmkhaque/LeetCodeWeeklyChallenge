class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = []
        
        for row in rectangle:
            temp = []
            for column in row:
                temp.append(column)
            self.rectangle.append(temp)
                    

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.rectangle[i][j] = newValue

        

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
        
