def check_win(list):
    if (list[0] == 'x') and (list[4] == 'x') and (list [8] == 'x'):
        return True
    elif (list[0] == 'x') and (list[3] == 'x') and (list [6] == 'x'):
        return True
    elif (list[0] == 'x') and (list[1] == 'x') and (list [2] == 'x'):
        return True
    elif (list[3] == 'x') and (list[4] == 'x') and (list [5] == 'x'):
        return True
    elif (list[6] == 'x') and (list[7] == 'x') and (list [8] == 'x'):
        return True
    elif (list[1] == 'x') and (list[4] == 'x') and (list [7] == 'x'):
        return True
    elif (list[2] == 'x') and (list[5] == 'x') and (list [8] == 'x'):
        return True
    elif (list[2] == 'x') and (list[4] == 'x') and (list [6] == 'x'):
        return True
    else:
        return False

def ploca(list) :
    print( '|' + list[0] + '|' + list[1] + '|' + list[2] + '|')
    print( ' -----')
    print( '|' + list[3] + '|' + list[4] + '|' + list[5] + '|')
    print( ' -----')
    print( '|' + list[6] + '|' + list[7] + '|' + list[8] + '|')

igraGotova = False
playerOneTurn = True
choices = []
polje = ['', '', '', '', '', '', '', '', '']

while not igraGotova :
    ploca(polje)

    if playerOneTurn :
        print( "Igrač 1:")
    else :
        print( "Igrač 2:")

    if False:
        choice = int(input(">> "))
    else:
        print("Unesi u prazno polje")
        continue
    if choices[choice - 1] == 'X' or choices[choice - 1] == 'O':
        print("Nemoguć potez")

    if playerOneTurn :
        choices[choice - 1] = 'X'
    else :
        choices[choice - 1] = 'O'

