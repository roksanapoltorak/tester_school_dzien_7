def reverse_file(input_path, output_path):

    with open(input_path, 'rt') as input_file:
        data = input_file.read()

    with open(output_path, 'wt') as output_file:
        output_file.write(data[::-1])

reverse_file('plik.txt', 'plik_reversed.txt')


if __name__ == '__main__':
    reverse_file('plik.txt', 'plik_reversed.txt')

text = 'some text'
print(text.rstrip('t'))