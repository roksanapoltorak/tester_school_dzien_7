import copy

class TabularData():

    def __init__(self, column_names):
        self.column_names = list(column_names)

        self._columns = {name: idx for idx, name  in enumerate(column_names)}

        if len(column_names) > len(self._columns):
            raise ValueError('Columns names have to be unique.')
        self._rows = []

    def get_row(self, row_no):
        if row_no < 0 or row_no >= len(self._rows):
            raise IndexError("Invalid row number: ", row_no)

        return self._rows[row_no]


    def get_column(self, col_name):

        if col_name not in self._columns:
            raise KeyError('Unknown column: ', col_name)

        idx = self._columns[col_name]

        return [row[idx] for row in self._rows]


    def append(self, new_row):

        if len(new_row) == len(self.column_names):
            self._rows.append(new_row)
        else:
            raise ValueError('Row should have size: ', len(self._columns))

    def rows_count(self):

        return len(self._rows)

    def to_list(self):
        return copy.deepcopy(self._rows)

    def __len__(self):
        return len(self._rows)

    def __str__(self):
        return str(self._rows)

table = TabularData(['Name', 'Surname', 'Age', 'Sex'])
table.append(['John', "Doe", 30, 'male'])
table.append(['Anna', 'Novak', 32, 'female'])
table.append(['Jack', 'Sparrow', 39, 'male'])
print(table._rows)

print(table.get_row(2))
print(table.get_column('Name'))

print(table.rows_count())

table.append(['Jane', 'Sorrrow', 29, 'female'])
print(table.to_list())

print(len(table))
print(str(table))