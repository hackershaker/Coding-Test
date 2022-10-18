from collections import defaultdict

if __name__=="__main__":
    string = input()
    dic = defaultdict(int)

    for word in string.split(" "):
        if word == "": continue
        dic[word] += 1

    print(sum(dic.values()))