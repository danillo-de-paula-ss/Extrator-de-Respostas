import pickle
import os
from glob import glob

# campos = []
# with open('campos.pkl', 'rb') as arquivo:
#     campos = pickle.load(arquivo)

# resp = []
# with open('resp.pkl', 'rb') as arquivo:
#     resp = pickle.load(arquivo)

# print(campos)
# print(resp)

# alternativas = 'abcde'.upper()
# x = alternativas * 10 + 'W'

# print(glob(os.path.join(os.path.dirname(__file__), 'tests', 'test2') + r'\*'))

# d = [[['63', '233', '17', '13,7', '', '', '', '', '', '', '', 55.0, True, False], ['63', '233', '17', '13,7', '', '', '', '', '', '', '', 55.0, True, False], ['63', '233', '17', '13,7', '', '', '', '', '', '', '', 55.0, True, False]], [['', '', '', '', '', '', '', '', '', '', '', 0.0, True, False], ['', '', '', '', '', '', '', '', '', '', '', 0.0, True, False], ['', '', '', '', '', '', '', '', '', '', '', 0.0, True, False]], [['', '', '', '', '', '', '', '', '', '', '', 0.0, True, False], ['', '', '', '', '', '', '', '', '', '', '', 0.0, True, False], ['', '', '', '', '', '', '', '', '', '', '', 0.0, True, False]], [['', '', '', '', '', '', '', '', '', '', '', 0.0, True, False], ['', '', '', '', '', '', '', '', '', '', '', 0.0, True, False], ['', '', '', '', '', '', '', '', '', '', '', 0.0, True, False]], [['', '', '', '', '', '', '', '', '', '', '', 0.0, True, False], ['', '', '', '', '', '', '', '', '', '', '', 0.0, True, False], ['', '', '', '', '', '', '', '', '', '', '', 0.0, True, False]]]

# # print(d[0])

# # print(','.join(['1', '2', ['3', '4']]))

# d = [[['A', 'A', 'A', 'A', 'B'], ['H', 'A', 'A', 'D', 'J'], ['D', 'A', 'F', 'G', 'H']], [['1', '3', '1', '3', '4', '3', '0', '4', '1', '0,1,2,3,4', '1', '3', '0', '3', '2', '4', '2', '0', '1', '1', '3', '1', '4', '1', '4', '1', '1', '3', '0', '2', '4', '2', '1', '0', '0', '0', '2', '4', '1', '2', '3', '2', '3', '2', '0', '0', '4', '2', '3', '2', '0', '4', '1', '0', '4', '3', '4', '0', '0', '0,1,2,3,4', '3', '3', '1', '2', '4', '2', '1', '0', '2', '0,1,2,3,4', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 
# '', '', '', '', '', '', '', '', '', ''], ['1', '1', '1', '3', '4', '3', '0', '2', '0', '3', '2', '3', '0', '3', '2', '4', '2', '0', '1', '4', '2', '3', '2', '0', '4', '1', '0', '', '3', '4', '1', '0', '0', '1', '3', '1', '3', '0', '1', '4', '3', '1', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], ['1', '1', '1', '2', '0', '4', '1', '4', '1', '3', '0', '3', '0', '1', '3', '1', '1', '0', '1', '4', '3', '0', '4', '4', '4', '4', '1', '3', '0', '3', '4', '3', '1', '0', '0', '0', '4', '4', '3', '2', '0', '2', '3', '1', '3', '1', '4', '2', '3', '3', '0', '3', '1', '4', '1', '3', '3', '2', '1', '0', '3', '2', '4', '1', '1', '1', '4', '3', '1', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']]]

# # print(*[';'.join([';'.join(k[index]) for k in d]) + '\n' for index in range(len(d[0]))])

# g = [['A', 'A', 'A', 'A', 'B'], ['H', 'A', 'A', 'D', 'J'], ['D', 'A', 'F', 'G', 'H']]

# print([[''.join(k)] for k in g])

d = [[[[1], [3], [1], [3], [4], [3], [0], [4], [1], [0, 1, 2, 3, 4], [1], [3], [0], [3], [2], [4], [2], [0], [1], [1], [3], [1], [4], [1], [4], [1], [1], [3], [0], [2], [4], [2], [1], [0], [0], [0], [2], [4], [1], [2], [3], [2], [3], [2], [0], [0], [4], [2], [3], [2], [0], [4], [1], [0], [4], [3], [4], [0], [0], [0, 1, 2, 3, 4], [3], [3], [1], [2], [4], [2], [1], [0], [2], [0, 1, 2, 3, 4], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], [[1], [1], [1], [3], [4], [3], [0], [2], [0], [3], [2], [3], [0], [3], [2], [4], [2], [0], [1], [4], [3], [0], [4], [4], [4], [4], [1], [3], [0], [3], [4], [3], [1], [0], [0], [0], [4], [4], [3], [2], [3], [2], [3], [2], [0], [1], [4], [2], [3], [2], [0], [4], [1], [0], [], [3], [4], [1], [0], [0], [1], [3], [1], [3], [0], [1], [4], [3], [1], [0], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], [[1], [1], [1], [2], [0], [4], [1], [4], [1], [3], [0], [3], [0], [1], [3], [1], [1], [0], [1], [4], [3], [0], [4], [4], [4], [4], [1], [3], [0], [3], [4], [3], [1], [0], [0], [0], [4], [4], [3], [2], [0], [2], [3], [1], [3], [1], [4], [2], [3], [3], [0], [3], [1], [4], [1], [3], [3], [2], [1], [0], [3], [2], [4], [1], [1], [1], [4], [3], [1], [0], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], [[1], [1], [1], [3], [4], [3], [0], [2], [1], [3], [1], [3], [3], [3], [2], [4], [2], [0], [1], [4], [3], [0], [4], [4], [4], [1], [1], [0], [0], [3], [4], [2], [1], [0], [0], [0], [2], [4], [3], [2], [3], [2], [2], [2], [0], [3], [4], [2], [3], [2], [0], [0], [0], [0], [4], [3], [4], [0], [0], [0], [1], [4], [1], [2], [4], [2], [1], [0], [1], [0], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], [[1], [3], [3], [3], [2], [3], [0], [2], [0], [3], [2], [3], [0], [3], [2], [4], [2], [0], [1], [4], [3], [0], [4], [4], [4], [4], [1], [3], [0], [3], [0], [1], [1], [0], [1], [0], [2], [4], [1], [3], [0], [2], [3], [2], [0], [1], [4], [2], [3], [2], [0], [4], [1], [0], [4], [3], [4], [1], [0], [0], [1], [3], [1], [3], [0], [1], [4], [3], [1], [0], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []]]

# print(len(d[0][5]))

print(os.path.splitext(r'D:\MyProjects\servicos\cliente001\prints'))
