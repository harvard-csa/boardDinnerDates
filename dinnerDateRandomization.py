import random
import scipy.stats as ss
import math

BOARD = ['Danika', 'Hannah', 'Amy', 'Chris',
        'Kathy', 'Carol', 'Alvin', 'Will', 
        'David', 'Tex', 'Kalos', 'Glen',
        'Shwe', 'Vick', 'Margo', 'Audrey G', 
        'Eric', 'Janice', 'Daniel', 'Cody', 
        'Christy', 'Steph', 'Audrey K', 'Christina',
        'Ricky', 'Sernea', 'Sophia']
GROUP_SIZE = 4
boardSize = len(BOARD)
EVEN_OUT_INDEX = 24
history = {}

def initialize():
    randomNums = [random.random() for _ in range(boardSize)]
    
    # converts random floats to rank ordering
    ranks = ss.rankdata(randomNums)
    
    # matches a random number 1-30 to board members
    board = zip(BOARD, ranks)
    
    # sort members by random number (1-4 is a group, 2-8...)
    board = sorted(board, key = lambda p: p[1])
    
    
    for i in range(0, boardSize, 4):
        tmp = [board[i][0], board[i+1][0], board[i+2][0]]
        if i != EVEN_OUT_INDEX:
            tmp += [board[i+3][0]]
        if 'Chris' in tmp and 'Christina' in tmp or sorted(tmp) in history.values():
            print('redo')
            return('redo')
        
    for i in range(0, boardSize, 4):
        tmp = [board[i][0], board[i+1][0], board[i+2][0]]
        if i != EVEN_OUT_INDEX:
            tmp += [board[i+3][0]]
        history[len(history)] = sorted(tmp)
        (print(', '.join(tmp)))
        

if __name__ == "__main__":
    for i in range(1,17):
        print("Week", i)
        while initialize() == 'redo':
            pass