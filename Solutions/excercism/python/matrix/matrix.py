class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.process_matrix_string()

    def row(self, index):

        return self.matrix_row[index-1]

    def column(self, index):
        column = []
        for row in self.matrix_row:
            column.append(row[index-1])
        return column

    def _process_matrix_string(self) :
        self.matrix_row = []
        rows = self.matrix_string.splitlines()
        for row in rows :
            new_row  = [int(x) for x in row.split()]
            self.matrix_row.append(new_row)
