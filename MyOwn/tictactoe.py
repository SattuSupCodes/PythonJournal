'''we will slowly build a tic tac toe game here as we keep learning python'''

'''THIS IS A WORK IN PROGRESS
I WILL MAKE THIS MYSELF STEP BY STEP'''

# we first create a 1-D board

board=[['_']*3 for i in range(3)]
print(board)
board[1][2]='x'
print(board)

choice=input("choose: ")
if(choice=='x'or 'X'):
    print(choice)
else:
    print("hoehoe")
    
'''we need to make it look like a tic tac toe board now with user inputs'''
'''we can use NumPy to create the matrix for the board 3x3'''

position=input("choose positions: ")
# smh
