import copy
import json

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

    def to_dict(self):
        return {'columns': self.column_names, 'rows': self._rows}

    @staticmethod
    def from_dict(data):
        table = TabularData(data['columns'])
        for row in data['rows']:
            table.append(row)
        return table

    def to_json(self):
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(json_data):
        return TabularData.from_dict((json.loads(json_data)))

    def to_json_file(self, output_file):

        return json.dump(self.to_dict(), output_file)

    @staticmethod
    def from_json_file(json_file):

        return TabularData.from_dict((json.load(json_file)))


table = TabularData(['Name', 'Surname', 'Age', 'Sex'])
table.append(['John', "Doe", 30, 'male'])
table.append(['Anna', 'Novak', 32, 'female'])
table.append(['Jack', 'Sparrow', 39, 'male'])

json_table = table.to_json()
table2 = TabularData.from_json(json_table)

print(table2.column_names == table.column_names)
print(table2._rows == table._rows)

print(table.to_json())
print(table2)

with open('table.json', 'wt') as json_file:
    table.to_json_file(json_file)

with open('table.json', 'rt') as json_file:
    table4 = TabularData.from_json_file(json_file)

print(table4.column_names == table.column_names)
print(table4._rows == table._rows)