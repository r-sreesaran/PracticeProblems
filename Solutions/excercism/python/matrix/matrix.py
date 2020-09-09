class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        matrix_row = self.process_matrix_string()
        return matrix_row[index-1]

    def column(self, index):
        matrix_row  = self.process_matrix_string()
        column = []
        for row in matrix_row:
            column.append(row[index-1])
        return column

    def process_matrix_string(self) :
        matrix_row = []
        rows = self.matrix_string.splitlines()
        for row in rows :
            new_row  = [int(x) for x in row.split()]
            matrix_row.append(new_row)
        return matrix_row 