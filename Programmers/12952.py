from opcode import stack_effect
from pprint import pprint
def solution(n):
    possible = set()

    def spin(arr): # rotate clockwise
        temp = []
        for a in arr:
            temp.append((a[1], n - a[0] -1))
        return frozenset(temp)

    def cutord(k):
        if k < 0 or k>=n: raise Exception
        else: return k
    
    #recursion
    def exp(ords, board):
        pprint(ords)
        if len(ords)==n:
            possible.add(frozenset(ords))
            return
        targetrow = ords[-1][0]+1
        for i in range(1,n):
            try: # left 
                board[ords[-1][0]][cutord(ords[-1][1]-i)] = 0
            except:
                pass
            try: # right
                board[ords[-1][0]][ords[-1][1]+i] = 0
            except: 
                pass
            try: # same column
                board[ords[-1][0]+i][ords[-1][1]] = 0
            except: 
                pass
            try: # left-down diagonal
                board[ords[-1][0]+i][cutord(ords[-1][1]-i)] = 0
            except:
                pass
            try: # right-down diagonal
                board[ords[-1][0]+i][ords[-1][1]+i] = 0
            except:
                pass 

        for i in range(n):
            # print(i)
            if board[targetrow][i] == 1:
                explore(ords+[(targetrow, i)], board)
                continue
        return

    def explore(ords, board):
        stack = [[ords, board]]
        while stack:
            path, brd = stack.pop()
            print(path)
            if len(path)==n:
                possible.add(frozenset(ords))
                continue
                
            targetrow = path[-1][0]+1
            for i in range(1,n):
                try: # left 
                    brd[path[-1][0]][cutord(path[-1][1]-i)] = 0
                except:
                    pass
                try: # right
                    brd[path[-1][0]][path[-1][1]+i] = 0
                except: 
                    pass
                try: # same column
                    brd[path[-1][0]+i][path[-1][1]] = 0
                except: 
                    pass
                try: # left-down diagonal
                    brd[path[-1][0]+i][cutord(path[-1][1]-i)] = 0
                except:
                    pass
                try: # right-down diagonal
                    brd[path[-1][0]+i][path[-1][1]+i] = 0
                except:
                    pass 
            # pprint(brd)
            print(targetrow)
            for i in range(n):
                if brd[targetrow][i] == 1:
                    stack.append([path+[(targetrow, i)], brd])

    for i in range(n):
        explore([(0,i)], [[1]*n for _ in range(n)])

    rotateset = set()
    for el in possible:
        spin_el = spin(el)
        rotateset.add(spin_el)
        spin_el = spin(el)
        rotateset.add(spin_el)
        spin_el = spin(el)
        rotateset.add(spin_el)

    possible |= rotateset
    # pprint.pprint(possible)

    return len(possible)

    
# print(solution(2), 0)
# print(solution(3), 0)
# print(solution(4), 2)
print(solution(5), 14)
# print(solution(6), 6)
# print(solution(7), 7)
# print(solution(8), 8)
# print(solution(9), 9)
# print(solution(10), 10)
# print(solution(11), 11)
# print(solution(12), 12)