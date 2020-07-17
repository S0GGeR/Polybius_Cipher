import sys
from PySide2 import QtCore, QtGui, QtWidgets
from pyside2 import Ui_Dialog


def i_alph():
    global alphabet
    alphabet = ui.alphabet.text().lower()


def i_power():
    global power
    power = int(ui.power.text())


def i_message():
    global message
    message = ui.message.text().lower()


def i_op():
    global op
    if ui.encryption.isChecked():
        op = 1
    elif ui.decryption.isChecked():
        op = 2


def polybius_cipher(square, word, op):
    for i in range(len(square)):
        for j in range(len(square[ i ])):
            print(square[ i ][ j ], end=' ')
        print()
    number = 0
    coords = [ ]
    while number < len(word):
        for i in range(len(square)):
            for j in range(len(square[ i ])):
                if (len(square[ i ][ j ])) == 1:
                    if word[ number ] == square[ i ][ j ]:
                        coords.append([ i, j ])
                        continue
                else:
                    for n in range(0, len(square[ i ][ j ])):
                        if word[ number ] == square[ i ][ j ][ n ]:
                            coords.append([ i, j ])
                            continue
        number += 1
    if len(coords) == 0:
        return None
    else:
        cipher = ''
        if op == 1:
            for coordinate in coords:
                if coordinate[ 0 ] == len(square) - 1:
                    coordinate[ 0 ] = 0
                elif square[ coordinate[ 0 ] + 1 ][ coordinate[ 1 ] ] == ' ':
                    coordinate[ 0 ] = 0
                else:
                    coordinate[ 0 ] += 1
            for i in range(0, len(word)):
                cipher += square[ coords[ i ][ 0 ] ][ coords[ i ][ 1 ] ]

            return cipher
        elif op == 2:
            for coordinate in coords:
                if coordinate[ 0 ] == 0:
                    print(len(square) - 1, coordinate[ 1 ], square[ 4 ][ 2 ])
                    if square[ len(square) - 1 ][ coordinate[ 1 ] ] == " ":
                        i = 0
                        while square[ len(square) - 1 - i ][ coordinate[ 1 ] ] == " ":
                            i += 1
                        coordinate[ 0 ] = len(square) - 1 - i
                    else:
                        coordinate[ 0 ] = len(square) - 1
                else:
                    coordinate[ 0 ] -= 1
            for i in range(0, len(word)):
                print(cipher, word, len(word), i)
                cipher += square[ coords[ i ][ 0 ] ][ coords[ i ][ 1 ] ]
                print(cipher, word, len(word), i)
            return cipher


def decomposition(numbers):
    array = [ ]
    for i in range(2, numbers):
        if numbers % i == 0:
            array.append([ i, int(numbers / i) ])
    if len(array) == 0:
        return None
    else:
        return array[ int((len(array) - 1) / 2) ]


def square_generator(alphabet, power, coord):
    i, j, number = 0, 0, 0

    square = [ ]
    if len(alphabet) > power:
        for i in range(0, coord[ 0 ]):
            square.append([ ])
            for j in range(0, coord[ 1 ]):
                square[ i ].append(alphabet[ number ])
                number = number + 1
        for i in range(len(square) - 1, -1, -1):
            for j in range(len(square[ i ]) - 1, -1, -1):

                if len(alphabet) - number == 0:
                    break
                else:
                    square[ i ][ j ] += alphabet[ number ]
                    number += 1
        while len(alphabet) - number > 0:
            for i in range(len(square) - 1, -1, -1):
                for j in range(len(square[ i ]) - 1, -1, -1):
                    if len(alphabet) - number == 0:
                        break
                    else:
                        square[ i ][ j ] += alphabet[ number ]
                        number += 1
        return square

    elif len(alphabet) <= power:
        for i in range(0, coord[ 0 ]):
            square.append([ ])
            for j in range(0, coord[ 1 ]):
                if number < len(alphabet):
                    square[ i ].append(alphabet[ number ])
                    number = number + 1
                else:
                    square[ i ].append(' ')
                    print(square)

        print(square)
        return square


def application_start():
    global alphabet, power, op, message
    if alphabet != '' and power != 0 and op != 0 and message != '':
        coord = decomposition(power)
        polybius_square = square_generator(alphabet, power, coord)
        result = polybius_cipher(polybius_square, message, op)
        ui.textBrowser.setText(str(polybius_square))
        ui.textBrowser_2.setText(result)


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
alphabet = ''
op = 0
message = ''
power = 0
ui.buttonGroup.buttonClicked.connect(i_op)
ui.alphabet.editingFinished.connect(i_alph)
ui.message.editingFinished.connect(i_message)
ui.power.editingFinished.connect(i_power)
ui.pushButton.clicked.connect(application_start)

sys.exit(app.exec_())

