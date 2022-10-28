if __name__=="__main__":
    N = int(input())
    people = list(map(int, input().split(" ")))
    people.sort()
    print( sum( [(N-i)*people[i] for i in range(len(people))] ) )