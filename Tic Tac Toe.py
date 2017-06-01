def check_winX(list):
    if (list[0] == 'X') and (list[4] == 'X') and (list [8] == 'X'):
        return True
    elif (list[0] == 'X') and (list[3] == 'X') and (list [6] == 'X'):
        return True
    elif (list[0] == 'X') and (list[1] == 'X') and (list [2] == 'X'):
        return True
    elif (list[3] == 'X') and (list[4] == 'X') and (list [5] == 'X'):
        return True
    elif (list[6] == 'X') and (list[7] == 'X') and (list [8] == 'X'):
        return True
    elif (list[1] == 'X') and (list[4] == 'X') and (list [7] == 'X'):
        return True
    elif (list[2] == 'X') and (list[5] == 'X') and (list [8] == 'X'):
        return True
    elif (list[2] == 'X') and (list[4] == 'X') and (list [6] == 'X'):
        return True
    else:
        return False

def check_winO(list):
    if (list[0] == 'O') and (list[4] == 'O') and (list [8] == 'O'):
        return True
    elif (list[0] == 'O') and (list[3] == 'O') and (list [6] == 'O'):
        return True
    elif (list[0] == 'O') and (list[1] == 'O') and (list [2] == 'O'):
        return True
    elif (list[3] == 'O') and (list[4] == 'O') and (list [5] == 'O'):
        return True
    elif (list[6] == 'O') and (list[7] == 'O') and (list [8] == 'O'):
        return True
    elif (list[1] == 'O') and (list[4] == 'O') and (list [7] == 'O'):
        return True
    elif (list[2] == 'O') and (list[5] == 'O') and (list [8] == 'O'):
        return True
    elif (list[2] == 'O') and (list[4] == 'O') and (list [6] == 'O'):
        return True
    else:
        return False

def drawPloca(list) :
    print('\n')
    print( '| ' + list[0] + ' | ' + list[1] + ' | ' + list[2] + ' |')
    print( ' -----------')
    print( '| ' + list[3] + ' | ' + list[4] + ' | ' + list[5] + ' |')
    print( ' -----------')
    print( '| ' + list[6] + ' | ' + list[7] + ' | ' + list[8] + ' |')
    print('\n')


playerOneTurn = True
pobjeda = False
polje = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

while not pobjeda:
    drawPloca(polje)

    upit = ''
    if playerOneTurn :
        upit = 'Igrač 1: '
    else:
        upit = 'Igrač 2: '

    unosIgrac = int(input(upit))
    unosIgrac = unosIgrac - 1

    if unosIgrac not in range(0, 9):
        print('Illegal move.')
        continue

    if polje[unosIgrac] == 'X' or polje[unosIgrac] == 'O':
        print('Space already full.')
        continue

    if playerOneTurn == True:
        polje[unosIgrac] = 'X'
    else:
        polje[unosIgrac] = 'O'

    playerOneTurn = not playerOneTurn

    pobjeda = check_winX(polje) or check_winO(polje)

    if check_winX(polje) == True:
        print ('Igrač 1 je pobjedio.')
        pobjeda = True

    if check_winO(polje) == True:
        print ('Igrač 2 je pobjedio.')
        pobjeda = True

drawPloca(polje)




