def check_win(p, c):
    if (p[0] == c) and (p[4] == c) and (p[8] == c):
        return True
    elif (p[0] == c) and (p[3] == c) and (p[6] == c):
        return True
    elif (p[0] == c) and (p[1] == c) and (p[2] == c):
        return True
    elif (p[3] == c) and (p[4] == c) and (p[5] == c):
        return True
    elif (p[6] == c) and (p[7] == c) and (p[8] == c):
        return True
    elif (p[1] == c) and (p[4] == c) and (p[7] == c):
        return True
    elif (p[2] == c) and (p[5] == c) and (p[8] == c):
        return True
    elif (p[2] == c) and (p[4] == c) and (p[6] == c):
        return True
    else:
        return False

def drawPloca(p) :
    print('\n')
    print( '| ' + p[0] + ' | ' + p[1] + ' | ' + p[2] + ' |')
    print( ' -----------')
    print( '| ' + p[3] + ' | ' + p[4] + ' | ' + p[5] + ' |')
    print( ' -----------')
    print( '| ' + p[6] + ' | ' + p[7] + ' | ' + p[8] + ' |')
    print('\n')

playerOneTurn = True
pobjeda = False
polje = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

while not pobjeda:
    drawPloca(polje)

    upit = ''
    if playerOneTurn:
        upit = 'Igrač 1: '
    else:
        upit = 'Igrač 2: '

    unosIgrac = int(input(upit)) - 1

    if unosIgrac not in range(0, 9):
        print('Protuzakonit potez.')
        continue

    if polje[unosIgrac] == 'X' or polje[unosIgrac] == 'O':
        print('Polje je već popunjeno.')
        continue

    if playerOneTurn:
        polje[unosIgrac] = 'X'
        if check_win(polje, 'X') == True:
            print('Igrač 1 je pobjedio!')
            pobjeda = True
    else:
        polje[unosIgrac] = 'O'
        if check_win(polje, 'O') == True:
            print('Igrač 2 je pobjedio!')
            pobjeda = True

    if '' in polje[1:9]:
        print('Izjednačeno, svi su gubitnici!')
        pobjeda = True
    else:
        pass

    playerOneTurn = not playerOneTurn

drawPloca(polje)




