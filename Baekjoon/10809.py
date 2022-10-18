if __name__=="__main__":
    s = input()
    answer = []
    for i in range(97, 123):
        answer.append(s.find(chr(i)))
    print(" ".join(map(str, answer)))
        