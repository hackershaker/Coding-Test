from enum import Enum
def solution(id_pw, db):
    class status(Enum):
        LOGIN = "login"
        FAIL = "fail"
        WRONG = "wrong pw"

    answer = ''
    for id, pw in db:
        if id == id_pw[0] and pw == id_pw[1]:
            answer =  status.LOGIN.value
            break
        if id == id_pw[0] and pw != id_pw[1]:
            return status.FAIL.value
    if answer == '': answer = status.WRONG.value
    return answer

print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))