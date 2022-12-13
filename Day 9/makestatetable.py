from statemachine import *


moves = {'UL': (-1,-1), 'UP': (-1,0), 'UR': (-1,1),
         'LEFT':  ( 0,-1),               'RIGHT' : (0, 1),
         'DL': ( 1,-1), 'DOWN': (1, 0), 'DR': ( 1,1)}

transitions = dict()
moved = dict()
for ii, ss in enumerate(stateDefs):
    for mm in moves.keys():
        newpos = (ss[0] + moves[mm][0], ss[1] + moves[mm][1])
        if newpos in stateDefs:
            transitions[(ii, mm)] = stateDefs.index(newpos)
            moved[(ii, mm)] = (0,0)
        else:
            if newpos[0] != 0 and newpos[1] != 0:
                delta = (newpos[0]//abs(newpos[0]), newpos[1]//abs(newpos[1]))
            elif newpos[0] == 0:
                delta = (0, newpos[1]//abs(newpos[1]))
            else: # newpos[1] == 0
                delta = (newpos[0]//abs(newpos[0]), 0)
            newstate = (newpos[0] - delta[0], newpos[1] - delta[1])
            transitions[(ii, mm)] = stateDefs.index(newstate)
            moved[(ii,mm)] = delta

# print("{", end='')
# for c, k in enumerate(moved.keys()):
#     print(f"{k}: {moved[k]}, ", end='')
#     if c%3 == 2:
#         print()

for k in statemachine.keys():
    if statemachine[k] != statemachine2[k]:
        print(f"statemachine key {k} is different")

for k in tchange.keys():
    if tchange[k] == tchange2[k]:
        print(f"tchange key {k} is OK")