def polybius_cipher(square, word):
    for i in range(len(square)):
        for j in range(len(square[i])):
            print(square[i][j], end=' ')
        print()
    number = 0
    coords = []
    while number < len(word):
        for i in range(len(square)):
            for j in range(len(square[i])):
                if (len(square[i][j])) == 1:
                    if word[number] == square[i][j]:
                        coords.append([i, j])
                        continue
                else:
                    for n in range(0, len(square[i][j])):
                        if word[number] == square[i][j][n]:
                            coords.append([i, j])
                            continue
        number += 1
    if len(coords) == 0:
        return None
    else:
        new_coords = []
        cipher = ''
        for i in range(0, len(coords), 2):
            if len(coords) - 1 == i:
                break
            new_coords.append([coords[i][0], coords[i + 1][0]])

        if len(coords) % 2 != 0:
            new_coords.append([coords[len(coords) - 1][0], coords[0][1]])
            for i in range(1, len(coords), 2):
                if len(coords) - 1 == i:
                    break
                new_coords.append([coords[i][1], coords[i + 1][1]])
        elif len(coords) % 2 == 0:
            for i in range(0, len(coords), 2):
                new_coords.append([coords[i][1], coords[i + 1][1]])

        for i in range(0, len(new_coords)):
            cipher += square[new_coords[i][0]][new_coords[i][1]]
        print(coords, new_coords)
        return cipher


def decomposition(numbers):
    array = []
    for i in range(2, numbers):
        if numbers % i == 0:
            array.append([i, int(numbers / i)])
    if len(array) == 0:
        return None
    else:
        return array[int((len(array) - 1) / 2)]


def square_generator(alphabet, power, coord):
    i, j, number = 0, 0, 0

    square = []
    if len(alphabet) > power:
        for i in range(0, coord[0]):
            square.append([])
            for j in range(0, coord[1]):
                square[i].append(alphabet[number])
                number = number + 1
        for i in range(len(square) - 1, -1, -1):
            for j in range(len(square[i]) - 1, -1, -1):

                if len(alphabet) - number == 0:
                    break
                else:
                    square[i][j] += alphabet[number]
                    number += 1
        while len(alphabet) - number > 0:
            for i in range(len(square) - 1, -1, -1):
                for j in range(len(square[i]) - 1, -1, -1):
                    if len(alphabet) - number == 0:
                        break
                    else:
                        square[i][j] += alphabet[number]
                        number += 1
        return square

    elif len(alphabet) <= power:
        for i in range(0, coord[0]):
            square.append([])
            for j in range(0, coord[1]):
                if number < len(alphabet):
                    square[i].append(alphabet[number])
                    number = number + 1
                else:
                    square[i].append(' ')
                    print(square)
            # if len(alphabet) != power:
            #     print(square)
            #     if len(square) < coord[0]:
            #         for i in range(0, len(square) - coord[0]):
            #             square.append([])
            #
            #         for i in range(0, coord[0]):
            #             for j in range(0, coord[1]):
            #                 print(i, j, coord[1], square)
            #                 if len(square[i]) < coord[1]:
            #                     square[i].append(' ')
        print(square)
        return square


status = 1
while status != 0:
    print('Вас приветствует программа для шифрования методом квадрата Полибия')
    status = int(input('Введите 1, если хотите продолжить работу, 0 для выхода из программы: \n'))
    if status == 0:
        break
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if len(alphabet) < 2:
        print('Извините, такой алфавит слишком короткий для шифрования сообщений. \
        Введите алфавит дейсвующего языка, пожалуйста')
        continue
    power = int(input('Введите мощность: \n'))
    coord = decomposition(power)
    if coord is None:
        print('Извините, такую мощность невозможно разложить на матрицу. Попробуйте снова')
        continue
    status = int(input('Введите 1 для шифрования, 2 для дешивроки, 0 для досрочного выхода из программы: \n'))
    if status == 1:
        message = (input('Введите сообщение для шифрования: \n').lower())
        polybius_square = square_generator(alphabet, power, coord)
        print(polybius_cipher(polybius_square, message))

    elif status == 2:
        alphabet = input('Введите алфавит: \n')
        power = input('Введите мощность: \n')
        message = input('Введите сообщение для дешифрования: \n')
        square_generator(alphabet, power)

    else:
        print('Ошибка ввода!')
