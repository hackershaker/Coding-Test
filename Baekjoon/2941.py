def solution(string:str) -> int:
    croaset = {'c=':"A", "c-":"B", "dz=":"C", "d-":"D", "lj":"E", "nj":"F", "s=":"G", "z=":"H"}
    
    for word in sorted(croaset, key = lambda x: len(x[0])):
        string = string.replace(word, croaset[word])
    print(len(string))
    return len(string)

if __name__=="__main__":
    answer = 0
    string = input()
    solution(string)