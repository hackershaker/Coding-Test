def solution2(n, costs): # 실패
    if n == 1: return 0
    answer = 0
    network = set()
    costs += [[x[1], x[0], x[2]] for x in costs]
    costs.sort(key = lambda x : (x[0], x[2]))
    print(costs)
    network.update([costs[0][0]]); answer += costs[0][2]
    while len(network) < n:
        for info in costs:
            if info[0] in network: continue
            if info[0] not in network and info[1] in network:
                print(f"new path {info[0]}---{info[1]} found! cost is {info[2]}")
                if any(path[2] < info[2] for path in costs if path[0]==info[1]): continue
                else:
                    network.add(info[0])
                    print(f"current network is {network}")
                    answer += info[2]
                    break
                
    return answer

def solution(n, costs):
    if n == 1: return 0
    answer = 0
    costs.sort(key = lambda x: (x[2], x[0]), reverse=True)
    print(costs)
    network = []
    while True:
        costinfo = costs.pop()
        for i in range(len(network)):
            if network[i] | {costinfo[0], costinfo[1]} == network[i]: break
            if len(network[i] & {costinfo[0], costinfo[1]}) != 0 :
                print(f"{network[i]} and {costinfo[0], costinfo[1]} is same network.")
                network[i] = network[i] | {costinfo[0], costinfo[1]}
                answer += costinfo[2]
                break
        else:
            print(f"same network not found, add {costinfo[0], costinfo[1]} to network")
            network.append({costinfo[0], costinfo[1]})
            answer += costinfo[2]
        
        try:
            for i in range(len(network)):
                if len(network[i] & network[i+1]) != 0:
                    network [i] = network[i] | network [i+1]
                    del network[i+1]
        except:
            pass    
        print("current network is : ", network)
        if len(network) == 1 and len(network[0]) == n: break
    
    return answer



# print(solution(1, []), 0)
# print(solution(3, [[0, 1, 2], [0, 2, 2], [1, 2, 3]]), 4)
# print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]), 4)
# print(solution(4, [[0, 1, 1], [0, 2, 2], [0, 3, 1], [1, 2, 1], [1, 3, 1], [2, 3, 2]]), 3)
# print(solution(5, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8], [4, 3, 2], [4, 2, 5], [4, 1, 4]]), 6)
# print(solution(5, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8], [4, 1, 4]]), 8)
# print(solution(5, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8], [4, 3, 2], [4, 2, 5], [4, 1, 4], [0, 3, 3], [0, 4, 1]]), 5)
# print(solution(5, [[0, 1, 1], [1, 2, 2], [2, 3, 5], [3, 4, 1]]), 9)
print(solution(4, [[0, 1, 1], [0, 2, 2], [0, 3, 1], [1, 2, 1], [1, 3, 1], [2, 3, 2]]), 3)
                                                    