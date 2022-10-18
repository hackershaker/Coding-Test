from collections import Counter
def solution(string):
    c = Counter(string.upper()).most_common()
    if len(c) == 1 or c[0][1] != c[1][1]:
        print(c[0][0])
        return c[0][0]
    if c[0][1] == c[1][1]: 
        print("?")
        return "?"

if __name__=="__main__":
    string = input()
    solution(string)
    