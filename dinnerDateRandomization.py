import random
import scipy.stats as ss
import math

class Member:
  def __init__(self, name, id):
    self.name = name
    self.id = id

board = ["Kathy", "Matthew", 'Danika', 'Hannah', 
        'Audrey K', 'Christina', 'Ricky', 'Steph', 
        'Chris', 'Alvin', 'Chao', 'David', 
        'Vick', 'Tex', 'Kalos', 'Carol', 
        'Sophia', 'Amy', 'Serena', 'Daran', 
        'Jasmine', 'Joy', 'Emily',
        'Glen', 'Shwe', 'Margo', 'Eric',
        'Audrey G', 'Daniel', 'Christy']
groupSize = 4
evenOut = 28

randomNums = [random.random() for x in range(len(board))]
ranks = ss.rankdata(randomNums)
for i in range(len(board)):
    if ranks[i] == evenOut:
        board[i] = Member(board[i], math.ceil(ranks[i]/groupSize + 1))
    else:
        board[i] = Member(board[i], math.ceil(ranks[i]/groupSize))
board.sort(key=lambda x: x.id)

for i in range(len(board)):
    if i > 0 and board[i].id != board[i-1].id:
        print('\n')
    print(board[i].name)