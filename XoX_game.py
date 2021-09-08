# This code is written by Abdullah Sağlık.
# saglikabd@gmail.com
# Istanbul/ Turkey
tahta = [['---', '---', '---'],
        ['---', '---', '---'],
        ['---', '---', '---']]  # The board is defined

kazanma = [[['0,0'],['0,1'],['0,2']],
          [['1,0'],['1,1'],['1,2']],
          [['2,0'],['2,1'],['2,2']],
          [['0,0'],['1,0'],['2,0']],
          [['0,1'],['1,1'],['2,1']],
          [['0,2'],['1,2'],['2,2']],
          [['0,0'],['1,1'],['2,2']],
          [['0,2'],['1,1'],['2,0']]]  # Conditions of win

# Lists are empty for memory
bos_X = []
bos_O = []
yeni_X = []
yeni_O = []

# Turn method
sira = 1

# The end condition
t = True

# The board is printed at screen.
print('\n')
print('The Board'.center(54))
print('--'*27,'\n|','|'.rjust(52))
print('|','|'.rjust(52))
for i in tahta:
    print('|'.ljust(0),'\t'.expandtabs(18),*i,'|'.rjust(21),'\n|','|'.rjust(52))
print('|','|'.rjust(52))
print('--'*27,'\n')

# The game is started with while loop.
while t:
    # Who's turn
    if sira % 2 == 1:
        print("X's turn!\n")
    else:
        print("O's turn!\n")

    # Inputing
    x = int(input('Your turn, input a Horizontal index [0,1,2]:'))
    y = int(input('Your turn, input a Vertical   index [0,1,2]:'))

    # Checking inputs for in range(3), else user will try again.
    if x in range(3) and y in range(3):

        # Checking the filled areas and make same user try again. Also turning is decreased with -1!!
        if ['{},{}'.format(x, y)] in bos_X or ['{},{}'.format(x, y)] in bos_O:
            print('\nPlease try again, it was filled.')
            sira -= 1
        else:
            if sira % 2 == 1:
                bos_X += [['{},{}'.format(x, y)]]
                tahta[x][y] = 'X'.center(3)
            else:
                bos_O += [['{},{}'.format(x, y)]]
                tahta[x][y] = 'O'.center(3)

        # The board looks like after inputs.
        print('\n')
        print('The Board'.center(54))
        print('--'*27,'\n|','|'.rjust(52))
        print('|','|'.rjust(52))
        for i in tahta:
            print('|'.ljust(0),'\t'.expandtabs(18),*i,'|'.rjust(21),'\n|','|'.rjust(52))
        print('|','|'.rjust(52))
        print('--'*27,'\n')

        # Turning
        sira += 1

        # Checking the winner
        bosluk = 0
        for i in tahta:
            if '---' in i:
                bosluk += 1
        if bosluk == 0:
            print('\nWithdraw! Game is over!')
            t= False
            break

        for i in kazanma:
            for z in i:
                for k in bos_X:
                    if z == k:
                        yeni_X += z
                for k in bos_O:
                    if z == k:
                        yeni_O += z
            if len(yeni_X) == len(i):
                print('\nX is the winner.....')
                print(yeni_X)
                t = False
                break
            elif len(yeni_O) == len(i):
                print('\nO is the winner.....')
                print(yeni_O)
                t = False
                break
            yeni_X.clear()  # yeni_X= []
            yeni_O.clear()  # yeni_O= []
    else:
        if x not in range(3):
            print('\nPlease input an index for Horizontal in range(3) again!')
        else:
            print('\nPlease input an index for Vertical   in range(3) again!')

print('\n\nThanks for playing this game.')

#ekstra
#print('X için girilmiş değerler:')
#print(bos_X,'\n')
#print('O için girilmiş değerler:')
#print(bos_O,'\n')

