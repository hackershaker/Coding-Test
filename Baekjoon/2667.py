from collections import deque
def solution():
    T = int(input())
    map = []
    for _ in range(T):
        map.append(input())
    networklist = []
    ordset = {(i,j) for i in range(T) for j in range(T)}
    
    while ordset:
        ord = ordset.pop()
        if map[ord[0]][ord[1]] == '1':
            network = {ord}
            ordset.discard(ord)
            stack = deque([ord])
            while stack:
                point = stack.popleft()
                u, d, r, l = (point[0]-1,point[1]), (point[0]+1,point[1]), (point[0],point[1]+1), (point[0],point[1]-1)

                for nextord in u,d,r,l:
                    if 0 <= nextord[0] < T and 0 <= nextord[1] < T and map[nextord[0]][nextord[1]] == '1' and nextord not in network:
                        network.add(nextord)
                        stack.append(nextord)
                    ordset.discard(nextord)
            networklist.append(len(network))
        else:
            ordset.discard(ord)
    
    print(len(networklist))
    networklist.sort()
    for net in networklist:
        print(net)
    return networklist

if __name__=="__main__":
    ans = solution()