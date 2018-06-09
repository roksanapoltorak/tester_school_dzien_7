def lines_histogram(input_path):

    histogram = {}

    with open(input_path, 'rt') as my_file:
        for line in my_file:
            stripped = line.rstrip('\r\n')

            histogram[len(stripped)] = histogram.get(len(stripped), 0) + 1

    return histogram

def lines_hist2(input_file):
    result = {}

    for line in input_file:
        key = len(line.strip('\r\n'))
        result[key] = result.get(key, 0) + 1
    return result


if __name__== '__main__':
    path = input("Podaj ścieżkę: ")
    try:
        print(lines_histogram(path))
    except OSError as err:
        print(err)


    try:
        with open(path, 'rt') as in_file:
            print(lines_hist2(in_file))
    except OSError as err:
        print(err)
