def read_input_file():
    the_tomb = open('input.txt')
    tomb_structure = the_tomb.readlines()

    tomb_parameters = tomb_structure[0]
    width = int(tomb_parameters.split(' ')[0])
    height = int(tomb_parameters.split(' ')[1])

    return width, height, tomb_structure


def find_all_routes():
    width, height, structure = read_input_file()
    print('Bizarre information about the tomb, found on the ancient script:\n', width, ' x ', height)
    floor = [x[:width] for x in structure[1:]]
    print(floor)
    paths = [[0 for k in range(width)] for k in range(height)]

    for x in range(width):
        for y in range(height):
            if x == 0:
                paths[y][x] = 1
                continue
            if floor[y][x] != floor[y][x - 1]:
                current = paths[y][x - 1]
            else:
                current = 0

            for i in range(height):
                for j in range(x):
                    if floor[y][x] == floor[i][j]:
                        current += paths[i][j]

            paths[y][x] = current
    if height > 1:
        safe_paths = paths[0][-1] + paths[-1][-1]
    else:
        safe_paths = paths[0][-1]
    print('\nNumber of all possible routes without getting unalived: ', safe_paths)


if __name__ == '__main__':
    find_all_routes()
