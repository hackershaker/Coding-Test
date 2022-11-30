from collections import defaultdict
def solution():
    answer = 0
    n = int(input())
    stairs = [int(input()) for _ in range(n)]
    dic = defaultdict(list)
    dic[1].append( [[1], stairs[0]] )
    if n >= 2: dic[2].append( [[2], stairs[1]] )
    
    for i in range(2, n+1):
        temp1max = [[], 0]
        for info in dic[i-1]:
            steps, total = info
            if len(steps) == 1 or steps[-1] - steps[-2] != 1:
                if temp1max[1] < total+stairs[i-1]:
                    temp1max = [ [steps[-1], steps[-1]+1], total+stairs[i-1] ]
        dic[i].append(temp1max)

        if dic.get(i-2, None):
            temp2max = [[], 0]
            for info in dic[i-2]:
                steps, total = info
                if temp2max[1] < total+stairs[i-1]:
                    temp2max = [ [steps[-1], steps[-1]+2], total+stairs[i-1] ]
                dic[i].append( [ [steps[-1], steps[-1]+2], total+stairs[i-1] ] )
            dic[i].append(temp2max)

    answer = max([x[1] for x in dic[n]])
    return answer

if __name__=="__main__":
    answer = solution()
    print(answer)